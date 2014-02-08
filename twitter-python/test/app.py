from twython import Twython

# Requires Authentication as of Twitter API v1.1

APP_KEY = '9KRXhSjKwXYJi2aKLX8Tsw'
APP_SECRET = '7dLz3IU79vZ5VzP2nr0njKV1cVJH57uajKKah5wtjwk'
OAUTH_TOKEN = '371304372-3P6gPluGU6yHcgE1GDsWr5CAZWo29sLj3aRNiUvJ'
OAUTH_TOKEN_SECRET = 'eW3MzVl9wug8EcZ6im3kuL0tZgx3crXq29yNl1Fvzlf7Y'

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

usuario = "ediqp8"
followers = twitter.get_followers_ids(screen_name = usuario) 

#print(twitter.get_followers_ids()['ids']) # ids list of followers

#for follower_id in followers :
	#print followers['ids']

try:
    user_timeline = twitter.get_user_timeline(screen_name= usuario, count=40)
except TwythonError as e:
   print e

for tweets in user_timeline:
   print tweets['text'].encode('utf-8')