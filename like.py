import tweepy
import sys
import os
#import jsonpickle
class APIError(exception):
    pass


#authenticator, ill need to get the key and all
twiauth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
twipi = tweepy.API()
wfile = open('Datacol.txt','w') #ill be writing into this file
api = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
 #sets the auth, if makes sure it works
if (not api)
    raise APIError("Error with API." +'\n')

query
#Begin to get user data. It might be good to install geopy
place = str(input("What Country? Input 'None' if you do not want\n" +
                  "to have a location"))
#something to make this better is to install geopy to narrow a location down          
tweetqnty = int(input("How many Tweets? "))
maxtweet = int(input("Max Tweets? "))

if (place == "None"):
    places = api.geo_search(query=place, granularity="country") #issue here due to geopy
    placeid = places[0].id #get id of location

key = str(input("What is or are the key word(s)? Be sure to use 'OR'" +
                "to seperate Key words."))
#^ill turn this into a whole array and turn it into a string 

for tweet in tweepy.Cursor(api.search, q = key, amount = tweetqnty):
    wfile.write(tweet + '\n')
    
                              












