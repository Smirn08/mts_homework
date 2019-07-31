import sqlite3
import json



db = sqlite3.connect('tweets.db')
cursor = db.cursor()

cursor.execute('''CREATE TABLE Tweets (
                    name TEXT,
                    tweet_text TEXT,
                    country_code TEXT,
                    display_url TEXT,
                    lang TEXT,
                    created_at TEXT,
                    location TEXT
                )''')

with open('three_minutes_tweets.json.txt') as f:
    for line in f:
        tweet = json.loads(line)
        if 'user' in tweet:
            name = tweet['user']['screen_name']
            tweet_text = tweet['text']
            country_code = tweet['place']['country_code'] if tweet['place'] else None
            display_url = f'https://twitter.com/statuses/{tweet["id"]}'
            lang = tweet['lang']
            created_at = tweet['created_at']
            location = tweet['user']['location']

            cursor.execute('INSERT INTO Tweets VALUES (?,?,?,?,?,?,?)', (
                name, tweet_text, country_code, display_url, lang,
                created_at, location
            ))


cursor.execute('''ALTER TABLE Tweets
                    ADD COLUMN tweet_sentiment INTEGER''')

db.commit()
db.close()
