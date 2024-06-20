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

# Tworzenie histogramów dla wyników VADER
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Histogram dla 'neg'
neg_scores = df['vader_sentiment'].apply(lambda x: x['neg'])
axes[0, 0].hist(neg_scores, bins=20, alpha=0.7, color='red')
axes[0, 0].set_title('VADER Negative Sentiment')
axes[0, 0].set_xlabel('Score')
axes[0, 0].set_ylabel('Frequency')

# Histogram dla 'neu'
neu_scores = df['vader_sentiment'].apply(lambda x: x['neu'])
axes[0, 1].hist(neu_scores, bins=20, alpha=0.7, color='blue')
axes[0, 1].set_title('VADER Neutral Sentiment')
axes[0, 1].set_xlabel('Score')
axes[0, 1].set_ylabel('Frequency')

# Histogram dla 'pos'
pos_scores = df['vader_sentiment'].apply(lambda x: x['pos'])
axes[1, 0].hist(pos_scores, bins=20, alpha=0.7, color='green')
axes[1, 0].set_title('VADER Positive Sentiment')
axes[1, 0].set_xlabel('Score')
axes[1, 0].set_ylabel('Frequency')

# Histogram dla 'compound'
compound_scores = df['vader_sentiment'].apply(lambda x: x['compound'])
axes[1, 1].hist(compound_scores, bins=20, alpha=0.7, color='purple')
axes[1, 1].set_title('VADER Compound Sentiment')
axes[1, 1].set_xlabel('Score')
axes[1, 1].set_ylabel('Frequency')

plt.tight_layout()
plt.show()

# Filtracja wyników BERT na pozytywne i negatywne
positive_bert_count = df[df['bert_sentiment'].apply(lambda x: x['label']) == 'POSITIVE'].shape[0]
negative_bert_count = df[df['bert_sentiment'].apply(lambda x: x['label']) == 'NEGATIVE'].shape[0]

# Tworzenie histogramu dla BERT Sentiment
plt.figure(figsize=(10, 6))

labels = ['POSITIVE', 'NEGATIVE']
counts = [positive_bert_count, negative_bert_count]

plt.bar(labels, counts, color=['green', 'red'], alpha=0.7)

plt.xlabel('Sentiment')
plt.ylabel('Count')
plt.title('BERT Sentiment Distribution: POSITIVE vs NEGATIVE')
plt.show()
