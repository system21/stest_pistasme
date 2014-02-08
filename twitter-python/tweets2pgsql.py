from datetime import datetime
import time
from sys import argv
import json
from twython import Twython
import psycopg2


# Requires Authentication as of Twitter API v1.1
APP_KEY = '9KRXhSjKwXYJi2aKLX8Tsw'
APP_SECRET = '7dLz3IU79vZ5VzP2nr0njKV1cVJH57uajKKah5wtjwk'
OAUTH_TOKEN = '371304372-3P6gPluGU6yHcgE1GDsWr5CAZWo29sLj3aRNiUvJ'
OAUTH_TOKEN_SECRET = 'eW3MzVl9wug8EcZ6im3kuL0tZgx3crXq29yNl1Fvzlf7Y'
twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

#connecion a la base de datos
conn = psycopg2.connect(database="test3python", user="postgres",password="1234")
cursor = conn.cursor()


palabra='#pistasenmalestado'
#geo
#tweets = twitter.search(q = palabra , geocode='-12.04218,-77.05759,10000mi') 
#tweets = twitter.search(q = palabra,count=100) 
tweets = twitter.search(q = palabra) 
#print tweets
tweets = tweets['statuses']
print str(len(tweets))

for tweet in tweets:
	#print tweet
	#usuarios
	id_u = tweet['user']['id_str']
	name_u = tweet['user']['name']
	screen_name = tweet['user']['screen_name']
	profile_image_url = tweet['user']['profile_image_url']	
	estado_u = True
	#tweets
	id_t =tweet['id_str']
	retweeted = tweet['retweeted']
	retweet_count = tweet['retweet_count']
	text_t = tweet['text']
	created_at = tweet['created_at']
	source = tweet['source']
	latitud = 0
	longitud = 0
	imagen = 'img'
	estado_t = True
	#asigna dispositivo
	if(not source =='web'):
		source='mobil'
	#verifica cordenadas
	if (not tweet['geo'] is None):
		latitud = tweet['geo']['coordinates'][0]
		longitud = tweet['geo']['coordinates'][1]
	#Verifica imagen	
	if tweet['entities'].has_key("media"):
		imagen = tweet['entities']['media'][0]['media_url_https']
	else :
		imagen= 'None'

	print '***************************************'		
	#print id_u
	print name_u
	#print screen_name
	#print profile_image_url
	#print id_t
	print retweet_count
	#print retweeted
	#print text_t
	#print created_at
	#print source
	#print latitud
	#print longitud
	#print imagen
	created_at = created_at.replace(" +0000", "");	
	print created_at
	#GOOD TWITER CONVERT DATE
	#struct_time = time.strptime(created_at, "%a %b %d   %H:%M:%S %Y")
	#time.struct_time(tm_year=2014, tm_mon=2, tm_mday=3, tm_hour=10, tm_min=53, tm_sec=7, tm_wday=0, tm_yday=34, tm_isdst=-1)
	#created_at= '%s/%s/%s' %(struct_time.tm_mday,struct_time.tm_mon,struct_time.tm_year)
	#END GOOD TWITER CONVERT DATE
	
	#print type(time.mktime(datetime.strptime(created_at, '%a %b %d %H:%M:%S %Y').utctimetuple()))
	
	created_at_timestampt= time.mktime(datetime.strptime(created_at, '%a %b %d %H:%M:%S %Y').utctimetuple())

	print created_at

	if (not (retweeted or (text_t[:2] in 'RT'))):
		print 'insert'
		query ="SELECT registrar_tweet(%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s)"
		cursor.execute(query, (id_u,name_u,screen_name,profile_image_url,estado_u,id_t,text_t,created_at_timestampt,source,latitud,longitud,imagen,estado_t ))
		conn.commit()
cursor.close()
conn.close()
#json.dump(geojson, open('transporte-twiter.js', 'w'))
