from twython import Twython

# Requires Authentication as of Twitter API v1.1

APP_KEY = '9KRXhSjKwXYJi2aKLX8Tsw'
APP_SECRET = '7dLz3IU79vZ5VzP2nr0njKV1cVJH57uajKKah5wtjwk'
OAUTH_TOKEN = '371304372-3P6gPluGU6yHcgE1GDsWr5CAZWo29sLj3aRNiUvJ'
OAUTH_TOKEN_SECRET = 'eW3MzVl9wug8EcZ6im3kuL0tZgx3crXq29yNl1Fvzlf7Y'

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

usuario = "Rub21tk"
followers = twitter.get_followers_ids(screen_name = usuario) 

#timeline tweets
try:
    user_timeline = twitter.get_user_timeline(screen_name= usuario, count=40)
except TwythonError as e:
   print e

for tweets in user_timeline:
   print tweets['text'].encode('utf-8')

#list id users
followers = twitter.get_followers_ids(screen_name = usuario, count=100) 
followers = followers['ids']
print "The user has %s followers" % str(len(followers))
for follower_id in followers:
   print "User with ID %d is following  Rub21tk" % follower_id

#list users
followers_names = twitter.get_followers_list(screen_name = usuario, count=100) 
followers_names = followers_names['users']
for follower_name in followers_names:
   print follower_name['name'].encode('utf-8')