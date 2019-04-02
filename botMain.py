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

"""
runs through terminal but have to update the code with correct s

"""

import tweepy


""" 
Must link your Twitter account to our bot. Must create a Twitter Application and generate a Consumer Key,
Consumer Secret, Access Token, and Access Token Secret.
"""
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

"""
followBack makes sure to follow all your current followers
"""
def followBack():
    user = api.me()
    for follower in tweepy.Cursor(api.followers).items():
        follower.follow()
        print ("Followed everyone that is following " + user.name)
    
"""
searches Twitter for keyword and reTweets or favorites based on that keyword
"""

def reTweetFavorite():
    search = "Aimi" #This is the keyword you'll be searching for
    
    numberOfTweets = 2
    #This is the number of tweets you wish to interact with
    
    for tweet in tweepy.Cursor(api.search,search).items(numberOfTweets):
        try:
            tweet.retweet() #can replace this as tweet.favorite to favorite instead of retweeting
            print('Retweeted this tweet')
            
        except tweepy.TweepError as e:
            print(e.reason)
            
        except StopIteration:
            break
"""
Replies to Tweets based on keyword

"""
        
def reply():
    search ="Bang Dream Aimi"
    numberOfTweets = 2
    phrase = "<3" #What your response tweet will be
    
    for tweet in tweepy.Cursor(api.search,search).items(numberOfTweets):
        try:
            
            tweetId = tweet.user.id #id of tweet you're responding to 
            username = tweet.user.screen_name#user's username you're responding too.
            api.update_status("@"+username + " " + phrase,in_reply_to_status_id = tweetId)
            print("Replied with " + phrase + " to " +username)
            
        except tweepy.TweepError as e:
            print(e.reason)
            
        except StopIteration:
            break
            
            
        
        
