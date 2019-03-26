# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 13:22:06 2019
Twitter Bot A using Tweepy

This bot can
1. Follow everyone following you.
2. Favorite and Retweet a Tweet based on keywords
3. Reply to a user based on a keyword

@author: Raymond Chin
"""

import tweepy



consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


""" testing connection and making sure it program can connect to Twitter

user = api.me()
print(user.name)
"""

def followBack():
    user = api.me()
    for follower in tweepy.Cursor(api.followers).items():
        follower.follow()
        print ("Followed everyone that is following " + user.name)
    

def mainFunction():
    search = "Aimi" #This is the keyword you'll be searching for
    
    numberOfTweets = 200
    #This is the number of tweets you wish to interact with
    
    for tweet in tweepy.Cursor(api.search,search).items(numberOfTweets):
        try:
            tweet.retweet() #can replace this as tweet.favorite to favorite instead of retweeting
            print('Retweeted this tweet')
            
        except tweepy.TweepError as e:
            print(e.reason)
            
        except StopIteration:
            break
        
        
mainFunction()