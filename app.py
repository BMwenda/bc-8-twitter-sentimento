"""
Twitter-Sentimento
Usage:
    twit get
    twit quit
    twit (-i | --interactive)
    twit (-h | --help | --version)
Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
"""

import json
import sys
import cmd
from twitter import *
import time
import datetime
from pprint import pprint
import operator
from collections import Counter
from nltk.corpus import stopwords
import string
from nltk.tokenize import word_tokenize
import nltk_helper
import utils
from pyfiglet import figlet_format
from termcolor import cprint, colored


config_file = open("config_dev.json", "r")
config = json.loads(config_file.read())

consumer_key = config["consumer_key"]
consumer_secret = config["consumer_secret"]
access_token = config["access_token"]
access_token_secret = config["access_token_secret"]

twitter = Twitter(auth = OAuth(access_token, access_token_secret, consumer_key, consumer_secret))

punctuation = list(string.punctuation)
stop = stopwords.words('english') + punctuation + ['rt', 'via']

def intro_to_project():
    print('\t ')
    cprint(figlet_format("Its All Twitter Senti"), 'cyan')
    print('+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+')
    print('\t\t Hey Twitter Lovers')
    print('\t Peek on what happens on your timeline and other people too')
    print('. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ')
    print('\t\t For any help please print help then enter')
    print('-------------------------------------------------------------------------')

def remove_stop_words():
    tweets = read_from_json()
    terms_with_no_stop = [term for term in nltk_helper.preprocess(tweets) if term not in stop]

    return terms_with_no_stop

def get_tweets():
    twitter_handle = ""
    max_number_of_tweets = 0
    twitter_handle = utils.sanitised_input("Enter username: ", str)
    max_number_of_tweets = utils.sanitised_input("Enter max number of tweets: ", int)
    
    tweets = twitter.statuses.user_timeline(screen_name=twitter_handle, count=max_number_of_tweets)

    for i in utils.progressbar(tweets, "Download in Progress", 50):
        time.sleep(0.1)

    print("Download of tweets complete!")
    print("Fetched {} tweets from {} Time Line".format(len(tweets), twitter_handle))

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

def get_top_five_terms():
    count_all = Counter()
    terms_all = remove_stop_words()
    count_all.update(terms_all)
    return count_all.most_common(10)

def get_word_count():
    count_all = Counter()
    terms_all = remove_stop_words()
    count_all.update(terms_all)
    return count_all.most_common()

def get_hash_tags():
    count_all = Counter()
    tweets = remove_stop_words()
    terms_hash = [term for term in tweets if term.startswith("#")]
    count_all.update(terms_hash)
     

    return count_all.most_common(20)

def get_single_terms():
    tweets = remove_stop_words()
    terms_single = set(tweets)

    return terms_single

def get_terms_only_with_no_mentions():
     tweets = remove_stop_words()
     terms_only = [term for term in tweets if term not in stop and not term.startswith(("#", "@"))]

     return terms_only


def main():
    intro_to_project()
    tweets = get_tweets()
    save_to_json(tweets)

    time.sleep(3)

    #do_analysis = input("Click yes to do some analysis (y/n): ")

    #if(do_analysis == "y" or "Y"):
    print("Lets do a little analysis of this tweets:\n")
    print("All the words in the tweet with their occurrences in descending:\n")
    pprint(get_word_count(), width=80)
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("\n")
    print("\n")

    print("Top five words in the tweets:\n")
    pprint(get_top_five_terms())
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("\n")
    print("\n")

    print("Hash tags in our tweets:\n")
    pprint(get_hash_tags())
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("\n")
    print("\n")


if __name__ == "__main__":
    main()