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
import utils

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

    for i in utils.progressbar(tweets, "Download in Progress", 50):
        time.sleep(0.1)

    print("Download of tweets complete!")
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

def get_single_terms():
    tweets = remove_stop_words()
    terms_single = set(tweets)

    return terms_single

def get_terms_only_with_no_mentions():
     tweets = remove_stop_words()
     terms_only = [term for term in tweets if term not in stop and not term.startswith(("#", "@"))]

     return terms_only

def print_it(my_list):
    for item in my_list:
        print(item + "\n")


def main():
    tweets = get_tweets("BBCNews", 500)
    save_to_json(tweets)

    do_analysis = input("Click yes to do some analysis (y/n): ")

    if(do_analysis == "y" or "Y"):
        print("Lets do a little analysis of this tweets:\n")
        print("All the words in the tweet with their occurrences in descending:\n")
        print(get_word_count())
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("\n")
        print("\n")

        print("Top words five words in the tweets:\n")
        print(get_top_five_terms())
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("\n")
        print("\n")

        print("Hash tags in our tweets:\n")
        print(get_hash_tags())
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("\n")
        print("\n")

    #print_it(get_top_five_terms())
    #print_it(get_hash_tags())
    #print(get_terms_only_with_no_mentions())
    #print_it(get_single_terms())

if __name__ == "__main__":
    main()