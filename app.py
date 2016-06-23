import json
import config
from twitter import *
import time
import datetime
from pprint import pprint
import panda as pd
import operator
from collections import Counter
from nltk.corpus import stopwords

config_file = open("config_dev.json", "r")
config = json.loads(config_file.read())

consumer_key = config["consumer_key"]
consumer_secret = config["consumer_secret"]
access_token = config["access_token"]
access_token_secret = config["access_token_secret"]

twitter = Twitter(auth = OAuth(access_token, access_token_secret, consumer_key, consumer_secret))

def get_tweets(twitter_handle, max_number_of_tweets):
    tweets = twitter.statuses.user_timeline(screen_name = twitter_handle, count=max_number_of_tweets)
    #user_tweets = str(json.loads(tweets))

    return tweets


def save_to_json(data):
    with open("tweets.json", "w") as out_file:
        json.dump(data, out_file)

def read_from_json():
    json_data = open("tweets.json").read()

    data = json.loads(json_data)
    tweet_list = []
    for dictionary in data:
        tweet_list.append(dictionary["text"])

    return tweet_list


save_to_json(get_tweets("Mwaniki", 10))
#print(read_from_json_and_return_text_list())

my_list = read_from_json()
#print(my_list[0])
#for text in my_list:
    #print(text)