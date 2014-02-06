from datetime import datetime
import time
from sys import argv
import json
from twython import Twython

# Requires Authentication as of Twitter API v1.1
APP_KEY = '9KRXhSjKwXYJi2aKLX8Tsw'
APP_SECRET = '7dLz3IU79vZ5VzP2nr0njKV1cVJH57uajKKah5wtjwk'
OAUTH_TOKEN = '371304372-3P6gPluGU6yHcgE1GDsWr5CAZWo29sLj3aRNiUvJ'
OAUTH_TOKEN_SECRET = 'eW3MzVl9wug8EcZ6im3kuL0tZgx3crXq29yNl1Fvzlf7Y'

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
palabra='#pistasenmalestado'
geojson = { "type": "FeatureCollection", "features": [] }
#geo
#tweets = twitter.search(q = palabra , geocode='-12.04218,-77.05759,10000mi') 
tweets = twitter.search(q = palabra,count=100) 
#print tweets
tweets = tweets['statuses']
print str(len(tweets))

for tweet in tweets:
	print tweet
	data = {
    "type": "Feature",
    "geometry": {
        "type": 'Point',
        "coordinates": []
    },
    "properties": { }
    }
	if (not tweet['retweeted']):
		if (not tweet['geo'] is None):
			data['geometry']['coordinates'].append(tweet['geo']['coordinates'][1])
			data['geometry']['coordinates'].append(tweet['geo']['coordinates'][0])
			data['properties']['user']=tweet['user']['screen_name']
			data['properties']['fecha']=tweet['created_at'].encode('utf-8')
			data['properties']['text']=tweet['text']
        	geojson['features'].append(data)
        else:
			print tweet['geo']


json.dump(geojson, open('transporte-twiter.js', 'w'))
		#print tweet['created_at'].encode('utf-8')
		#print tweet['retweeted']   			
   		#print tweet['text']
   		#print tweet['user']['screen_name']
