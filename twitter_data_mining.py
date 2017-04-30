# import all modules
from pymongo import MongoClient
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from datetime import datetime
import json

# Connect to mongoDB
client = MongoClient('localhost', 27017)
db = client['mgo_db']
collection = db['time100_collection']


# Set the twitter API keys and tokens
consumer_key="#########################"
consumer_secret="##################################################"
access_token="##################################################"
access_token_secret="#############################################"


# Define a listener handles tweets that are received from the stream.
# This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        tweet = json.loads(data)
        try:
            tweet_id = collection.insert_one(tweet).inserted_id
            print(tweet_id)
        except:
            pass
        return True

    def on_error(self, status):
        print(status)

# Define the main function.
if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
# Set the track list.
    track_list = ['TIME100']
    stream.filter(track = track_list)
