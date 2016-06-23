import json
import config
from twitter import *
import time
import datetime
from pprint import pprint
import operator
from collections import Counter
import sanitize_helper
from nltk.corpus import stopwords
import string
from nltk.tokenize import word_tokenize
import nltk_helper

config_file = open("config_dev.json", "r")
config = json.loads(config_file.read())

consumer_key = config["consumer_key"]
consumer_secret = config["consumer_secret"]
access_token = config["access_token"]
access_token_secret = config["access_token_secret"]

twitter = Twitter(auth = OAuth(access_token, access_token_secret, consumer_key, consumer_secret))

punctuation = list(string.punctuation)
stop = stopwords.words('english') + punctuation + ['rt', 'via']

def remove_stop_words():
    tweets = read_from_json()
    terms_with_no_stop = [term for term in nltk_helper.preprocess(tweets) if term not in stop]

    return terms_with_no_stop

def get_tweets(twitter_handle, max_number_of_tweets):
    tweets = twitter.statuses.user_timeline(screen_name = twitter_handle, count=max_number_of_tweets)

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

    tweets_sentence = ", ".join(tweet_list)
    return tweets_sentence
    #return tweet_list

#def remove_stop_words():
    #data = read_from_json().split()

    #filtered_words = sanitize_helper.sanitize(data, sanitize_helper.stop_words)

    #return filtered_words

#def remove_stop_words_2():
    #data = read_from_json().split()

    #stop = stopwords.words("english")
    #print([i for i in data if i not in stop])

def get_top_five_terms():
    count_all = Counter()
    terms_all = remove_stop_words()
    count_all.update(terms_all)
    return count_all.most_common(5)

def get_word_count():
    count_all = Counter()
    terms_all = remove_stop_words()
    count_all.update(terms_all)
    return count_all.most_common()

def get_hash_tags():
     tweets = remove_stop_words()
     terms_hash = [term for term in tweets if term.startswith("#")]

     return terms_hash

def get_terms_only_with_no_mentions():
     tweets = remove_stop_words()
     terms_only = [term for term in tweets if term not in stop and not term.startswith(("#", "@"))]

     return terms_only


#print(len(get_stop_words()))
#get_first_tweet()
get_top_five_terms()
#print(get_hash_tags())
#print(get_terms_only_with_no_mentions())