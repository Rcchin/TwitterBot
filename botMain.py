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



consumer_key = '22oIME1Q9yoGbswjpb38lDJKM'
consumer_secret = 'J9f8cENZ9d1yPm5Eaz5lPxJ17Trq1yhwI1oLJpk8wmoRzyvybc'
access_token = '1730350868-68GuCNQiDHOUqdizNevqgTNpvmddBPqiq4pXvS3'
access_token_secret = 'EY8GvOsnFmpNJByZqve4WQnABe8mruRnbuVoXeCptCycO'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


""" testing connection and making sure it program can connect to Twitter

user = api.me()
print(user.name)
"""

for follower in tweepy.Cursor(api.followers).items():
    follower.follow()
    print ("Followed everyone that is following " + user.name)
    
    
