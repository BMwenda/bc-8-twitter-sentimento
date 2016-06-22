import json
import config
from twitter import *
import time
import datetime

config_file = open("config_dev.json", "r")
config = json.loads(config_file.read())

consumer_key = config["consumer_key"]
consumer_secret = config["consumer_secret"]
access_token = config["access_token"]
access_token_secret = config["access_token_secret"]

twitter = Twitter(auth = OAuth(access_token, access_token_secret, consumer_key, consumer_secret))

user_tweets = []

def get_tweets(twitter_handle, max_number_of_tweets):
    tweets = twitter.statuses.user_timeline(screen_name = twitter_handle, count=max_number_of_tweets)
    #user_tweets = str(json.loads(tweets))

    return tweets

def get_tweets_2(twitter_handle, from_date, to_date):
    tweets = twitter.statuses.user_timeline(screen_name=twitter_handle, since=from_date, until=to_date)
    #user_tweets = str(json.loads(tweets))

    return tweets


def save_to_json(data, handle):
    with open("{}_tweets.json".format(handle), "w") as out_file:
        json.dump(data, out_file)


#for status in user_tweets:
    #print("(%s) %s" % (status["id"], status["text"].encode("ascii", "ignore")))

#for status in results:
    #print("(%s) %s" % (status["created_at"], status["text"].encode("ascii", "ignore")))

#get_tweets("Mwaniki", "2016-01-01", )
save_to_json(get_tweets_2("Mwaniki", "2016-01-01", "2016-02-02"), "mwaniki")
#save_to_json(user_tweets)
