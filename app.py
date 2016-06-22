import json
import tweepy
import oauth_handler

auth = oauth_handler.getAuth()
   
api  = tweepy.API(auth)

user_tweets = []

def save_to_json(data):
    with open("tweets.json", "w") as out_file:
        json.dump(data, out_file)


def twitter_fetch(screen_name = "BBCNews", maxnumtweets=200):
    'Fetch tweets from @BBCNews'

    tweets = tweepy.Cursor(api.user_timeline, id=screen_name).items(50)
    for status in tweets:
        print(status.text + "\n")
        user_tweets.append(status.text)

    return user_tweets
    #save_to_json(user_tweets)

  

if __name__ == '__main__':
    twitter_fetch('@Mwaniki')
    save_to_json(user_tweets)