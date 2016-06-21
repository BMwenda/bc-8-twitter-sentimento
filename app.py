import json
import tweepy
from tweepy import OAuthHandler

#Twitter Credentials
consumer_key = "gPD2ZjrRaXY6OKSWiza5YQJOg"
consumer_secret = "KaPXywbktbNeOzpegQzDHAQp2qnpicgcCLqnzw451BsxdmQGYx"
access_key = "272311979-SWU6JF7TM62mGFn2ZC3xN8Fh6nQHB22cngAuMc1I"
access_secret = "A6gqoojWr8TYuJMXVDKxb892uM7HJeCoP8b4rkmTi3PZ0"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)

api = tweepy.API(auth)

for status in tweepy.Cursor(api.home_timeline).items(10):
    #Process a single status
    print(status.text)