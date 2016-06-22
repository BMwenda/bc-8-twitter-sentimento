import json
import config
from twitter import *
import config

consumer_key="gPD2ZjrRaXY6OKSWiza5YQJOg"
consumer_secret="KaPXywbktbNeOzpegQzDHAQp2qnpicgcCLqnzw451BsxdmQGYx"
access_token="272311979-SWU6JF7TM62mGFn2ZC3xN8Fh6nQHB22cngAuMc1I"
access_token_secret="A6gqoojWr8TYuJMXVDKxb892uM7HJeCoP8b4rkmTi3PZ0"

twitter = Twitter(auth = OAuth(access_token, access_token_secret, consumer_key, consumer_secret))

user_tweets = {}

def get_tweets(twitter_handle, max_number_of_tweets):
    results = twitter.statuses.user_timeline(screen_name = twitter_handle, count=max_number_of_tweets)

    return results


def save_to_json(data):
    with open("json_data_file.json", "w") as out_file:
        json.dump(data, out_file)

#with open("json_data.json", "r") as in_file:
    #json.load()

#for status in results:
    #print("(%s) %s" % (status["created_at"], status["text"].encode("ascii", "ignore")))

#get_tweets("Mwaniki", 15)
save_to_json(get_tweets("Mwaniki", 15))
