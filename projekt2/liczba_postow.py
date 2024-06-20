import json
import os
from datetime import datetime
import matplotlib.pyplot as plt

# Lista nazw plików JSON
file_names = [
    'analysis_results.json', 'analysis_results_po_1_sezonie.json', 'analysis_results2.json', 'analysis_results3.json', 'analysis_results4.json',
    'analysis_results6.json', 'analysis_results7.json', 'analysis_results8.json', 'analysis_results9.json', 'analysis_results10.json'
]

# Przygotowanie przedziałów czasowych dla osi X
time_intervals = [
    '10.2019 - 12.2019', '12.2019 - 06.2020', '06.2020 - 12.2020', '12.2020 - 06.2021', '06.2021 - 12.2021',
    '12.2021 - 06.2022', '06.2022 - 12.2022', '12.2022 - 06.2023', '06.2023 - 12.2023', '12.2023 - 06.2024'
]

# Lista przechowująca liczbę obiektów JSON w każdym pliku
json_counts = []

# Iteracja przez listę nazw plików
for file_name in file_names:
    # Utworzenie ścieżki do pliku
    file_path = os.path.join('', file_name)  # Zastąp 'path_to_your_directory' swoją ścieżką

    # Otwarcie pliku i wczytanie danych JSON
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Zliczenie liczby obiektów JSON w pliku
    json_count = len(data)

    # Dodanie wyniku do listy
    json_counts.append(json_count)

# Przygotowanie danych do wykresu
x = range(len(file_names))  # x to numeracja plików
y = json_counts

# Stworzenie wykresu liniowego
plt.figure(figsize=(10, 6))
plt.plot(x, y, marker='o', linestyle='-', color='b', label='Number of JSON Objects')
plt.xticks(x, time_intervals, rotation=45)  # Ustawienie etykiet na osi X jako przedziały czasowe
plt.xlabel('Time Intervals')
plt.ylabel('Number of JSON Objects')
plt.title('Number of JSON Objects in Each File')
plt.grid(True)
plt.tight_layout()
plt.legend()
plt.show()
