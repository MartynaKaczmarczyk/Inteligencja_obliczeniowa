import praw
import json
import pandas as pd
from datetime import datetime, timedelta

# Inicjalizacja klienta praw
reddit = praw.Reddit(client_id='SVsShQ3qAhC2ejX3KpetTQ',
                     client_secret='Sz_8ZDsFBqDaCcLzxLcu7JheZIwT8g',
                     user_agent='app'
                     )
subreddits = [ 'witcher', 'netflixwitcher', 'fantasy', 'television', 'gaming', 'cosplay']
keywords = ['Witcher', 'witcher', 'Wiedźmin', 'witcher', 'Ciri', 'Jaskier', 'Yarpen', 'Geralt', 'Yennefer', 'Triss', 'Nilfgaard', 'Tissaia', 'Dziki gon', 'Time of Contempt']

post_limit = 2000  # Łączna liczba postów do pobrania

start_date = datetime(2023, 12, 29)  # Początkowa data
end_date = datetime(2024, 6, 16)    # Końcowa data

def is_within_date_range(post_date):
    post_datetime = datetime.fromtimestamp(post_date)
    return start_date <= post_datetime <= end_date

posts = []
count = 0

for subreddit_name in subreddits:
    for keyword in keywords:
        print(f'Pobieranie postów z subreddita: {subreddit_name} dla słowa kluczowego: {keyword}')
        for submission in reddit.subreddit(subreddit_name).search(keyword, limit=None):
            if count >= post_limit:
                break
            if is_within_date_range(submission.created):
                post_data = {
                    'title': submission.title,
                    'score': submission.score,
                    'id': submission.id,
                    'url': submission.url,
                    'num_comments': submission.num_comments,
                    'created_utc': submission.created_utc,
                    'created_date': datetime.fromtimestamp(submission.created_utc).isoformat(),
                    'body': submission.selftext
                }
                posts.append(post_data)
                count += 1
                print(f'Pobrano {count} postów...')
        if count >= post_limit:
            break
    if count >= post_limit:
        break

# Zapisanie postów do pliku JSON
with open('reddit_posts2024_today_10.json', 'w') as file:
    json.dump(posts, file, indent=4)

print(f'Pomyślnie pobrano {len(posts)} postów i zapisano do pliku reddit_diy_posts.json')