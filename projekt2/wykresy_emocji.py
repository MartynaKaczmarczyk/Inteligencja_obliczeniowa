import json
import pandas as pd
import matplotlib.pyplot as plt

# Wczytanie danych JSON
with open('analysis_results10.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Tworzenie DataFrame
df = pd.DataFrame(data)

# Przekształcanie kolumny 'created_date' na datetime
df['created_date'] = pd.to_datetime(df['created_date'])

# Wyodrębnianie emocji z text2emotion
emotions = ['Happy', 'Angry', 'Surprise', 'Sad', 'Fear']
emotion_counts = {emotion: df['text2emotion_emotions'].apply(lambda x: x[emotion]).sum() for emotion in emotions}
emotion_means = {emotion: df['text2emotion_emotions'].apply(lambda x: x[emotion]).mean() for emotion in emotions}

# Tworzenie wykresu słupkowego porównującego ilość każdej emocji
plt.figure(figsize=(10, 6))
plt.bar(emotion_counts.keys(), emotion_counts.values(), color=['yellow', 'red', 'orange', 'blue', 'purple'], alpha=0.7)

plt.xlabel('Emotion')
plt.ylabel('Count')
plt.title('Distribution of Emotions in Posts')
plt.show()

# Wyświetlanie średnich dla każdej emocji
print("Average of each emotion:")
for emotion, mean in emotion_means.items():
    print(f"{emotion}: {mean:.4f}")
