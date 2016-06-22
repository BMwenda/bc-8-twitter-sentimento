# module oath
import tweepy


#Twitter credentials
consumer_key="gPD2ZjrRaXY6OKSWiza5YQJOg"
consumer_secret="KaPXywbktbNeOzpegQzDHAQp2qnpicgcCLqnzw451BsxdmQGYx"
access_token="272311979-SWU6JF7TM62mGFn2ZC3xN8Fh6nQHB22cngAuMc1I"
access_token_secret="A6gqoojWr8TYuJMXVDKxb892uM7HJeCoP8b4rkmTi3PZ0"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


def getAPI():
	api = tweepy.API(auth)
	print("DEBUG: is no logged in!".format(api.me().name))
	return api

def getAuth():
    return auth