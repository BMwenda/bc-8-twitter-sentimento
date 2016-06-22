import tweepy
import json

from tweepy import OAuthHandler

#Twitter API credentials
consumer_key = "gPD2ZjrRaXY6OKSWiza5YQJOg"
consumer_secret = "KaPXywbktbNeOzpegQzDHAQp2qnpicgcCLqnzw451BsxdmQGYx"
access_key = "272311979-SWU6JF7TM62mGFn2ZC3xN8Fh6nQHB22cngAuMc1I"
access_secret = "A6gqoojWr8TYuJMXVDKxb892uM7HJeCoP8b4rkmTi3PZ0"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)
file = open('today.txt', 'a')

# file name that you want to open is the second argument
save_file = open('9may.json', 'a')

class CustomStreamListener(tweepy.StreamListener):
    # initialize blank list to contain tweets
    tweets = []

    def __init__(self, api):
        self.api = api
        super(tweepy.StreamListener, self).__init__()

        self.save_file = tweets

    def on_status(self, status):
        print(status.text)

    def on_data(self, tweet):
        self.save_file.append(json.loads(tweet))
        print(tweet)
        save_file.write(str(tweet))

    def on_error(self, status_code):
        print >> sys.stderr, 'Encountered error with status code:', status_code
        return True # Don't kill the stream

    def on_timeout(self):
        print >> sys.stderr, 'Timeout...'
        return True # Don't kill the stream

sapi = tweepy.streaming.Stream(auth, CustomStreamListener())
sapi.filter(track=['python'])