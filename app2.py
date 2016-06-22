### code to save tweets in json###
import sys
import tweepy
import json
import config

consumer_key=config.consumer_key
consumer_secret=config.consumer_secret
access_key = config.access_token
access_secret = config.access_token_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)
file = open('today.txt', 'a')

class CustomStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        print(status.text)

    def on_data(self, data):
        json_data = json.loads(data)
        file.write(str(json_data))

    def on_error(self, status_code):
        #print >> sys.stderr, 'Encountered error with status code:', status_code
        return True # Don't kill the stream

    def on_timeout(self):
        #print >> sys.stderr, 'Timeout...'
        return True # Don't kill the stream

sapi = tweepy.streaming.Stream(auth, CustomStreamListener())
sapi.filter(follow=['1469402426', '612473', '278134121'])