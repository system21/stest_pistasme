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
conn = psycopg2.connect(database="pythontest", user="postgres",password="1234")
cursor = conn.cursor()


palabra='#pistasenmalestado'
geojson = { "type": "FeatureCollection", "features": [] }
#geo
#tweets = twitter.search(q = palabra , geocode='-12.04218,-77.05759,10000mi') 
tweets = twitter.search(q = palabra,count=100) 
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
	print id_u
	print name_u
	print screen_name
	print profile_image_url

	#tweets
	id_t =tweet['id_str']
	retweeted = tweet['retweeted']
	text_t = tweet['text']
	created_at = tweet['created_at']
	source = tweet['source']
	latitud = 12.4
	longitud = 74.15
	imagen = 'img'
	estado_t = True

	print id_t
	print retweeted
	print text_t
	print created_at
	print source

	if (not retweeted):
		query ="SELECT registrar_tweet(%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s)"
		cursor.execute(query, (id_u,name_u,screen_name,profile_image_url,estado_u,id_t,text_t,created_at,source,latitud,longitud,imagen,estado_t ))
		conn.commit()
	#query_verifica = "SELECT check_usuario(%s);"
	#cursor.execute(query_verifica, (id,)) #nose porque la coma al final pero asi funciona
	#verifica_existencia = cursor.fetchone()
	
	#query = "INSERT INTO usuario(id, name, screen_name, profile_image_url, estado) VALUES (%s, %s, %s, %s, %s);"
	#cursor.execute(query, (id, name, screen_name,profile_image_url,estado))
	#conn.commit()
	#print verifica_existencia
cursor.close()
conn.close()





#json.dump(geojson, open('transporte-twiter.js', 'w'))
		#print tweet['created_at'].encode('utf-8')
		#print tweet['retweeted']   			
   		#print tweet['text']
   		#print tweet['user']['screen_name']