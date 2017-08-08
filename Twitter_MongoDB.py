from twython import TwythonStreamer
from pymongo import MongoClient


consumer_key = 'consumer_key here'
consumer_secret = 'consumer_secret here'
access_token = 'access_token here'
access_token_secret = 'access_token_secret here'

db = MongoClient('localhost').twitter_db

class MyStreamer(TwythonStreamer):
	def on_success(self, data):
		print data
		db.myNewCollection1.insert(data)

		
	def on_error(self, status):
		print status

		
stream = MyStreamer(consumer_key, consumer_secret,
                    access_token, access_token_secret)

stream.statuses.filter(track = '#hashtag here')		