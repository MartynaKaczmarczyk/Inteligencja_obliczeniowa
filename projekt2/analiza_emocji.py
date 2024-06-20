import json
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import text2emotion as te
from transformers import pipeline
import matplotlib.pyplot as plt
from datetime import datetime

# Pobieranie dodatkowych danych dla VADER
nltk.download('vader_lexicon')

# Inicjalizacja VADER
sia = SentimentIntensityAnalyzer()

# Wczytanie danych JSON
with open('reddit_posts2019_20dec_jun.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Inicjalizacja modelu BERT do analizy sentymentu
sentiment_pipeline = pipeline("sentiment-analysis")


# Funkcja do analizy recenzji
def analyze_review(review_text):
    # Analiza sentymentu VADER
    vader_sentiment = sia.polarity_scores(review_text)

    # Analiza emocji Text2Emotion
    emotions = te.get_emotion(review_text)

    # Podział tekstu na fragmenty o maksymalnej długości 512 znaków
    max_length = 512
    chunks = [review_text[i:i + max_length] for i in range(0, len(review_text), max_length)]

    # Analiza sentymentu BERT dla każdego fragmentu i uśrednienie wyników
    bert_sentiment = {'label': 'neutral', 'score': 0}
    for chunk in chunks:
        result = sentiment_pipeline(chunk)[0]
        if result['label'] == 'POSITIVE':
            bert_sentiment['score'] += result['score']
        else:
            bert_sentiment['score'] -= result['score']

    # Normalizacja wyniku BERT
    bert_sentiment['score'] /= len(chunks)
    bert_sentiment['label'] = 'POSITIVE' if bert_sentiment['score'] > 0 else 'NEGATIVE'

    return vader_sentiment, emotions, bert_sentiment


# Listy do przechowywania wyników analizy i dat
dates = []
vader_scores = []
bert_scores = []
text2emotion_scores = []
analysis_results = []

# Analiza każdej recenzji z JSON-a
for item in data:
    review_text = item['title'] + ' ' + item.get('body', '')

    vader_sentiment, emotions, bert_sentiment = analyze_review(review_text)

    # Zbieranie wyników i dat
    created_date = datetime.strptime(item['created_date'], '%Y-%m-%dT%H:%M:%S')
    dates.append(created_date)
    vader_scores.append(vader_sentiment['compound'])
    bert_scores.append(bert_sentiment['score'])
    text2emotion_scores.append(emotions)

    # Dodawanie wyników analizy do listy
    analysis_results.append({
        'id': item['id'],
        'created_date': item['created_date'],
        'title': item['title'],
        'body': item.get('body', ''),
        'vader_sentiment': vader_sentiment,
        'text2emotion_emotions': emotions,
        'bert_sentiment': bert_sentiment
    })

    print(f"Review ID: {item['id']}")
    print("VADER Sentiment Analysis:", vader_sentiment)
    print("Text2Emotion Analysis:", emotions)
    print("BERT Sentiment Analysis:", bert_sentiment)
    print("\n" + "-" * 50 + "\n")

# Sortowanie wyników według daty
sorted_data = sorted(analysis_results, key=lambda x: x['created_date'])

# Rozpakowanie posortowanych danych
sorted_dates = [datetime.strptime(item['created_date'], '%Y-%m-%dT%H:%M:%S') for item in sorted_data]
sorted_vader_scores = [item['vader_sentiment']['compound'] for item in sorted_data]
sorted_bert_scores = [item['bert_sentiment']['score'] for item in sorted_data]
sorted_text2emotion_scores = [item['text2emotion_emotions'] for item in sorted_data]

# Zapisanie wyników analizy do pliku JSON
with open('analysis_results_po_1_sezonie.json', 'w', encoding='utf-8') as outfile:
    json.dump(sorted_data, outfile, ensure_ascii=False, indent=4)

# Wykres liniowy dla sentymentu VADER i BERT
plt.figure(figsize=(12, 6))
plt.plot(sorted_dates, sorted_vader_scores, label='VADER Sentiment', marker='o')
plt.plot(sorted_dates, sorted_bert_scores, label='BERT Sentiment', marker='o')
plt.xlabel('Date')
plt.ylabel('Sentiment Score')
plt.title('Sentiment Analysis Over Time')
plt.legend()
plt.show()

# Opcjonalnie: Wykres dla emocji z Text2Emotion
emotion_keys = sorted_text2emotion_scores[0].keys()
for emotion in emotion_keys:
    emotion_values = [scores[emotion] for scores in sorted_text2emotion_scores]
    plt.plot(sorted_dates, emotion_values, label=emotion, marker='o')

plt.xlabel('Date')
plt.ylabel('Emotion Score')
plt.title('Emotion Analysis Over Time')
plt.legend()
plt.show()
