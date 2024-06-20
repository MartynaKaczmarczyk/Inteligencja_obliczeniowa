import json
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Pobranie zasobu 'punkt' do tokenizacji zdań
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Wczytanie danych JSON
with open('reddit_posts2024_today_10.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Połączenie tekstów z pól 'title' i 'body' w jeden ciąg znaków
text = ' '.join(item['title'] + ' ' + item.get('body', '') for item in data)

tokens = word_tokenize(text)
num_tokens = len(tokens)
print(f"Liczba słów po tokenizacji: {num_tokens}")

# Pobranie listy angielskich stop-words
stop_words = set(stopwords.words('english'))

# Dodatkowe stop-words
additional_stop_words = {'said', 'will', 'also', '.', '#', ',','http','\'s', ']', '&','(', ')','--', '"','-','','[', "'",'', '*', ':', '?', '!', '`','’','WC', 'nt', 'like', '``', '\u2060The', 'WC','  ', '\'', '>', '|', '‘', 'http', ';', 'The', '1', '2', '3' }
stop_words.update(additional_stop_words)

# Ręczne usuwanie cudzysłowów i innych niechcianych znaków z tokenów
tokens = [word.replace('"', '').replace("'", '') for word in tokens]

filtered_tokens = [word for word in tokens if word.lower() not in stop_words]
num_filtered_tokens = len(filtered_tokens)
print(f"Liczba słów po usunięciu stop-words: {num_filtered_tokens}")

# Inicjalizacja lematyzera
lemmatizer = WordNetLemmatizer()

# Lematyzacja
lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]
num_lemmatized_tokens = len(lemmatized_tokens)
print(f"Liczba słów po lematyzacji: {num_lemmatized_tokens}")
word_freq = Counter(lemmatized_tokens)

# Wybór 10 najczęściej występujących słów
common_words = word_freq.most_common(10)
words = [word[0] for word in common_words]
frequencies = [word[1] for word in common_words]
print(frequencies, words)
plt.figure(figsize=(10, 6))
plt.bar(words, frequencies)
plt.xlabel('Słowa')
plt.ylabel('Liczba wystąpień')
plt.title('10 najczęściej występujących słów')
plt.show()

# Tworzenie chmury tagów
wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(word_freq)

# Wyświetlenie chmury tagów
plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
