import tweepy
import csv
import pandas as pd
import time
from textblob import TextBlob

def authenticate_user():
	# Create variables for each key, secret, token
	consumer_key = 'XXXXXXXXX'
	consumer_secret = 'XXXXXXXXX'
	access_token = 'XXXXXXX'
	access_token_secret = 'XXXXXXXX'
	# Set up OAuth and integrate with API
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth)
	return api
	
def cleanTweet(tweet):
	string=tweet.text.encode('utf-8')
	#clean hashtag
	for htg in tweet.entities['hashtags']:
		word=htg['text']
		word="#"+word
		string=string.replace(bytes(word,'utf-8'),bytes('','utf-8'))
	 #clean urls   
	for urll in tweet.entities['urls']:
		t_url=urll['url']
		string=string.replace(bytes(t_url,'utf-8'),bytes('','utf-8'))
	#clean tagged user	
	for usrr in tweet.entities['user_mentions']:
		t_usr=usrr['screen_name']
		t_usr="@"+t_usr
		string=string.replace(bytes(t_usr,'utf-8'),bytes('','utf-8'))
		
	string=string.replace(bytes("b'",'utf-8'),bytes('','utf-8'),1)
	string=string.replace(bytes('RT :','utf-8'),bytes('','utf-8'))
	return string

def checkSentiment(tweetText):
	analysis = TextBlob(tweetText)
	return analysis.sentiment.polarity
	
def getTweet(api,hashTag,fileName,startDT,numTweet=2):
	hashTag="\"#"+hashTag+"\""
	startDT="\""+startDT+"\""
	csvFile = open(fileName, 'w')
	csvWriter = csv.writer(csvFile)
	try:
		for tweet in tweepy.Cursor(api.search,q=hashTag,count=numTweet,lang="en",since=startDT).items():
			if tweet.retweeted==False:
				cleantweet=cleanTweet(tweet)
				csvWriter.writerow([tweet.created_at,tweet.user.screen_name,str(cleantweet),checkSentiment(str(cleantweet))])
	except:
		print("Unable to connect Twitter API.")		
	
api=authenticate_user()
getTweet(api,'370','tweetSentiment.csv','2019-07-23')
