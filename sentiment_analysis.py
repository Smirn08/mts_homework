import re
import sqlite3


def santiment_analysis(text):
    afinn_dict = {}
    with open('AFINN-111.txt') as f:
        for line in f:
            word, sentiment = line.split('\t')
            afinn_dict[word] = int(sentiment)

    sentiment = 0
    for word in re.findall('\w+', text):
        sentiment += afinn_dict.get(word.lower(), 0)

    return sentiment


db = sqlite3.connect('tweets.db')
cursor = db.cursor()

cursor.execute('''SELECT display_url, tweet_text
                    FROM Tweets
                ''')

result = cursor.fetchall()

for display_url, tweet_text in result:
    sentiment = santiment_analysis(tweet_text)
    cursor.execute('''UPDATE Tweets
                        SET tweet_sentiment = ?
                        WHERE display_url = ?''', (sentiment, display_url))

db.commit()
db.close()
