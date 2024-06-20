import json
import os
import glob
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Użycie backendu 'Agg'
plt.switch_backend('Agg')

# Ścieżka do katalogu z plikami JSON


# Definicja przedziałów czasowych
time_intervals = [
    ('10.2019 - 12.2019', '2019-10-01', '2019-12-31'),
    ('12.2019 - 06.2020', '2019-12-01', '2020-06-30'),
    ('06.2020 - 12.2020', '2020-06-01', '2020-12-31'),
    ('12.2020 - 06.2021', '2020-12-01', '2021-06-30'),
    ('06.2021 - 12.2021', '2021-06-01', '2021-12-31'),
    ('12.2021 - 06.2022', '2021-12-01', '2022-06-30'),
    ('06.2022 - 12.2022', '2022-06-01', '2022-12-31'),
    ('12.2022 - 06.2023', '2022-12-01', '2023-06-30'),
    ('06.2023 - 12.2023', '2023-06-01', '2023-12-31'),
    ('12.2023 - 06.2024', '2023-12-01', '2024-06-30')
]


# Funkcja do przypisywania przedziału czasowego na podstawie daty
def assign_time_interval(date_str):
    for interval, start, end in time_intervals:
        if start <= date_str <= end:
            return interval
    return None


# Inicjalizacja listy dla przechowywania danych
all_data = []
file_names = [
    'analysis_results.json', 'analysis_results_po_1_sezonie.json', 'analysis_results2.json', 'analysis_results3.json', 'analysis_results4.json',
    'analysis_results6.json', 'analysis_results7.json', 'analysis_results8.json', 'analysis_results9.json', 'analysis_results10.json'
]
# Wczytanie danych z każdego pliku JSON pasującego do wzorca 'analysis_result*.json'
for filepath in file_names:
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            json_data = json.load(file)
            for entry in json_data:
                entry['source_file'] = os.path.basename(filepath)
                entry['time_interval'] = assign_time_interval(entry.get('created_date', ''))
            all_data.extend(json_data)
    except Exception as e:
        print(f"Error reading {filepath}: {e}")

# Sprawdzenie, czy dane zostały wczytane poprawnie
if not all_data:
    print("No data loaded. Please check the files and their paths.")
else:
    print(f"Loaded {len(all_data)} records.")

# Utworzenie DataFrame z danych
df = pd.DataFrame(all_data)

# Sprawdzenie, jakie kolumny zawiera DataFrame
print("Columns in the DataFrame:", df.columns)

# Sprawdzenie pierwszych kilku rekordów
print("First few records in the DataFrame:")
print(df.head())


# Funkcja pomocnicza do tworzenia DataFrame z wartościami sentymentu
def extract_sentiment(df, sentiment_col, sentiment_name):
    sentiment_df = pd.concat([df[['id', 'source_file', 'time_interval']], df[sentiment_col].apply(pd.Series)], axis=1)
    sentiment_df = sentiment_df.melt(id_vars=["id", "source_file", "time_interval"], var_name="Component",
                                     value_name="Score")
    sentiment_df['Sentiment'] = sentiment_name

    # Konwersja wartości 'Score' na liczby zmiennoprzecinkowe
    sentiment_df['Score'] = pd.to_numeric(sentiment_df['Score'], errors='coerce')

    # Usunięcie wierszy z brakującymi lub nieprawidłowymi wartościami
    sentiment_df = sentiment_df.dropna(subset=['Score'])

    return sentiment_df


# Ekstrakcja i przetwarzanie danych z VADER
vader_df = extract_sentiment(df, 'vader_sentiment', 'VADER')

# Ekstrakcja i przetwarzanie danych z Text2Emotion
t2e_df = extract_sentiment(df, 'text2emotion_emotions', 'Text2Emotion')

# Ekstrakcja i przetwarzanie danych z BERT
bert_df = extract_sentiment(df, 'bert_sentiment', 'BERT')

# Połączenie wszystkich danych w jeden DataFrame
combined_df = pd.concat([vader_df, t2e_df, bert_df], axis=0)

# Obliczenie średniej dla każdego komponentu w każdym pliku
mean_scores = combined_df.groupby(['time_interval', 'Sentiment', 'Component'])['Score'].mean().reset_index()
mean_scores['source_file'] = 'Mean'

# Dodanie średnich do oryginalnych danych
combined_with_mean_df = pd.concat([combined_df, mean_scores], axis=0)

# Tworzenie wykresów
sns.set(style="whitegrid")


# Funkcja pomocnicza do tworzenia wykresów liniowych
def create_line_plot(data, sentiment, components):
    plt.figure(figsize=(14, 8))

    # Filtracja danych dla danego sentymentu
    sentiment_data = data[data['Sentiment'] == sentiment]

    # Wykresy dla każdego komponentu
    for component in components:
        component_data = sentiment_data[sentiment_data['Component'] == component]
        sns.lineplot(data=component_data, x='time_interval', y='Score', label=component)

    plt.title(f'{sentiment} Analysis')
    plt.xlabel('Time Interval')
    plt.ylabel('Score')
    plt.xticks(rotation=45, fontsize='small')  # Zmniejszenie rotacji i zmiana rozmiaru czcionki
    plt.legend(title='Component', loc='upper right')
    plt.tight_layout()  # Poprawa układu
    plt.savefig(f'{sentiment}_analysis.png')
    plt.show()


# Lista komponentów do wykresów
vader_components = ['neg', 'neu', 'pos', 'compound']
t2e_components = ['Happy', 'Angry', 'Surprise', 'Sad', 'Fear']
bert_components = ['label', 'score']

# Tworzenie wykresu liniowego dla VADER
create_line_plot(combined_with_mean_df, 'VADER', vader_components)

# Tworzenie wykresu liniowego dla Text2Emotion
create_line_plot(combined_with_mean_df, 'Text2Emotion', t2e_components)

# Tworzenie wykresu liniowego dla BERT
create_line_plot(combined_with_mean_df, 'BERT', bert_components)
