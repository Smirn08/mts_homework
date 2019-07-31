import sqlite3

db = sqlite3.connect('tweets.db')
cursor = db.cursor()

cursor.execute('''CREATE TABLE User (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    location_id INT REFERENCES Location (id)
                )''')

cursor.execute('''CREATE TABLE Location (
                    id INTEGER PRIMARY KEY,
                    location TEXT
                )''')

cursor.execute('''CREATE TABLE Country (
                    id INTEGER PRIMARY KEY,
                    country_code TEXT
                )''')

cursor.execute('''CREATE TABLE new_tweets_table (
                    display_url TEXT,
                    user_id INT REFERENCES User (id),
                    tweet_text TEXT,
                    lang TEXT,
                    country_id INT REFERENCES Country (id),
                    created_at TEXT,
                    tweet_sentiment INT
                )''')

cursor.execute('''INSERT INTO Location (location)
                    SELECT DISTINCT location
                    FROM Tweets
                ''')

cursor.execute('''INSERT INTO User (name, location_id)
                    SELECT name, Location.id
                    FROM Tweets
                    JOIN Location ON Location.location = Tweets.location
                    GROUP BY name
                ''')

cursor.execute('''INSERT INTO Country (country_code)
                    SELECT DISTINCT country_code
                    FROM Tweets
                ''')

cursor.execute('''INSERT INTO new_tweets_table (display_url, user_id, tweet_text, lang, country_id, created_at)
                    SELECT Tweets.display_url,
                            User.id,
                            Tweets.tweet_text,
                            Tweets.lang,
                            Country.id,
                            Tweets.created_at
                    FROM Tweets
                    LEFT JOIN User ON User.name = Tweets.name
                    LEFT JOIN Country ON Country.country_code = Tweets.country_code
                    GROUP BY Tweets.display_url
                ''')


cursor.execute('''DROP TABLE Tweets''')

cursor.execute('''ALTER TABLE new_tweets_table RENAME TO Tweets''')

db.commit()
db.close()
