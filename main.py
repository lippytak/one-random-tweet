from TwitterAPI import TwitterAPI
import os

# Load config
consumer_key = os.environ['CONSUMER_KEY']
consumer_secret = os.environ['CONSUMER_SECRET']
access_token_key = os.environ['ACCESS_TOKEN_KEY']
access_token_secret = os.environ['ACCESS_TOKEN_SECRET']

api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)

# Run this periodically (via Heroku scheduler)
def retweet_one_random_tweet():
	r = api.request('statuses/sample')
	tweet = r.get_iterator().next()
	
	try:
		tweet_id = tweet['id']
		possibly_sensitive = tweet['possibly_sensitive']
	except:
		possibly_sensitive = False
		return

	if possibly_sensitive:
		retweet = api.request('statuses/retweet/:%d' % tweet_id)

retweet_one_random_tweet()