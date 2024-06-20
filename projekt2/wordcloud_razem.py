import json
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import glob

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Initialize variables for combined text
combined_text = ''

# Load and concatenate text from 10 JSON files
file_list = glob.glob('reddit_posts*.json')
for file_name in file_list:
    with open(file_name, 'r', encoding='utf-8') as file:
        data = json.load(file)
        combined_text += ' '.join(item['title'] + ' ' + item.get('body', '') for item in data) + ' '

# Tokenization
tokens = word_tokenize(combined_text)
num_tokens = len(tokens)
print(f"Liczba słów po tokenizacji: {num_tokens}")

# Stopwords
stop_words = set(stopwords.words('english'))
additional_stop_words = {'said', 'will', 'also', '.', '#', ',', 'http', '\'s', ']', '&', '(', ')', '--', '"', '-', '', '[', "'", '', '*', ':', '?', '!', '`', '’', 'WC', 'nt', 'like', '``', '\u2060The', 'WC', '  ', '\'', '>', '|', '‘', 'http', ';', 'The', '1', '2', '3'}
stop_words.update(additional_stop_words)

# Remove unwanted characters from tokens
tokens = [word.replace('"', '').replace("'", '') for word in tokens]

# Remove stopwords
filtered_tokens = [word for word in tokens if word.lower() not in stop_words]
num_filtered_tokens = len(filtered_tokens)
print(f"Liczba słów po usunięciu stop-words: {num_filtered_tokens}")

# Lemmatization
lemmatizer = WordNetLemmatizer()
lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]
num_lemmatized_tokens = len(lemmatized_tokens)
print(f"Liczba słów po lematyzacji: {num_lemmatized_tokens}")

# Word frequency
word_freq = Counter(lemmatized_tokens)

# Most common words
common_words = word_freq.most_common(10)
words = [word[0] for word in common_words]
frequencies = [word[1] for word in common_words]
print(frequencies, words)

# Bar chart of most common words
plt.figure(figsize=(10, 6))
plt.bar(words, frequencies)
plt.xlabel('Słowa')
plt.ylabel('Liczba wystąpień')
plt.title('10 najczęściej występujących słów')
plt.show()

# Word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(word_freq)

# Display word cloud
plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
