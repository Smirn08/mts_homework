import sqlite3

db = sqlite3.connect('tweets.db')
cursor = db.cursor()

# happiest country
cursor.execute('''SELECT country_code, AVG(tweet_sentiment)
                    FROM Tweets
                    JOIN Country on Country.id = Tweets.country_id
                    GROUP BY country_code
                    ORDER BY AVG(tweet_sentiment) DESC
                    LIMIT 1
                ''')
HappiestCountry = cursor.fetchall()

# unhappiest country
cursor.execute('''SELECT country_code, AVG(tweet_sentiment)
                    FROM Tweets
                    JOIN Country on Country.id = Tweets.country_id
                    GROUP BY country_code
                    ORDER BY AVG(tweet_sentiment)
                    LIMIT 1
                ''')
UnhappiestCountry = cursor.fetchall()

# happiest location
cursor.execute('''SELECT location, AVG(tweet_sentiment)
                    FROM Tweets
                    JOIN User ON User.id = Tweets.user_id
                    JOIN Location ON Location.id = User.location_id
                    GROUP BY location
                    ORDER BY AVG(tweet_sentiment) DESC
                    LIMIT 3
                ''')
HappiestLocation = cursor.fetchall()

# unhappiest location
cursor.execute('''SELECT location, AVG(tweet_sentiment)
                    FROM Tweets
                    JOIN User ON User.id = Tweets.user_id
                    JOIN Location ON Location.id = User.location_id
                    GROUP BY location
                    ORDER BY AVG(tweet_sentiment)
                    LIMIT 1
                ''')
UnhappiestLocation = cursor.fetchall()

# happiest user
cursor.execute('''SELECT name, tweet_text, AVG(tweet_sentiment)
                    FROM Tweets
                    JOIN User ON User.id = Tweets.user_id
                    GROUP BY user_id
                    ORDER BY AVG(tweet_sentiment) DESC
                    LIMIT 1
                ''')
HappiestUser = cursor.fetchall()

# unhappiest user
cursor.execute('''SELECT name, tweet_text, AVG(tweet_sentiment)
                    FROM Tweets
                    JOIN User ON User.id = Tweets.user_id
                    GROUP BY user_id
                    ORDER BY AVG(tweet_sentiment)
                    LIMIT 1
                ''')
UnhappiestUser = cursor.fetchall()

db.commit()
db.close()

newline = '\n'

print(f'''Happiest country: {HappiestCountry[0][0]} | Average sentiment for tweets: {HappiestCountry[0][1]}
Unhappiest country: {UnhappiestCountry[0][0]} | Average sentiment for tweets: {UnhappiestCountry[0][1]}

Happiest location: {HappiestLocation[0][0]} | Average sentiment for tweets: {HappiestLocation[0][1]}
Unhappiest location: {UnhappiestLocation[0][0]} | Average sentiment for tweets: {UnhappiestLocation[0][1]}

Happiest user: {HappiestUser[0][0]} | Tweet: {HappiestUser[0][1].replace(newline," ")}
Unhappiest user: {UnhappiestUser[0][0]} | Tweet: {UnhappiestUser[0][1].replace(newline," ")}''')
