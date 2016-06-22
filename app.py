import json
import config
from twitter import *

consumer_key = config.consumer_key
consumer_secret = config.consumer_secret
access_token = config.access_token
access_token_secret = config.access_token_secret

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
