#import urllib, json
#import sys
import tweepy
from tweepy import OAuthHandler

#Twitter API credentials
consumer_key = "gPD2ZjrRaXY6OKSWiza5YQJOg"
consumer_secret = "KaPXywbktbNeOzpegQzDHAQp2qnpicgcCLqnzw451BsxdmQGYx"
access_key = "272311979-SWU6JF7TM62mGFn2ZC3xN8Fh6nQHB22cngAuMc1I"
access_secret = "A6gqoojWr8TYuJMXVDKxb892uM7HJeCoP8b4rkmTi3PZ0"

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_key,access_secret)
   
api  = tweepy.API(auth)


def twitter_fetch(screen_name = "BBCNews", maxnumtweets=200):
    'Fetch tweets from @BBCNews'

    tweets = tweepy.Cursor(api.user_timeline, id=screen_name).items(200)

    for status in tweets:
        print(status.text+'\n')

  

if __name__ == '__main__':
    twitter_fetch('RealDonaldTrump', 200)