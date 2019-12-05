# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 12:43:13 2019

@author: Chase
"""

import tweepy
import credentials
from textblob import TextBlob
from iexfinance.refdata import get_symbols
from iexfinance.stocks import Stock


auth = tweepy.OAuthHandler(credentials.CONSUMER_KEY, credentials.CONSUMER_SECRET)
auth.set_access_token(credentials.ACCESS_TOKEN, credentials.ACCESS_TOKEN_SECRET)


#Load stock symbols from api
get_symbols(output_format='pandas', token="sk_3bb7e1d66fb348399371ac0662e8672e")


# Take input for Stock Selection and Sentiment_Score -- Stock object is pulled from api
stock = input("What stock would you like to predict? ")
stock = stock.upper()
stock = Stock(stock, token = credentials.STOCK_SECRET_KEY)
sentiment_score = float(input("Please input sentiment score (-1.0 - 1.0: )"))


#Store all variables needed for prediction -- pulled from iexfinance stock api
day5Change = stock.get_key_stats().get("day5ChangePercent")
day5Change = round(day5Change,8)
prevOpen = stock.get_previous_day_prices().get("open")
prevClose = stock.get_previous_day_prices().get("close")
prevAvg = (prevOpen + prevClose) / 2
prevAvg = round(prevAvg,2)


amount5Change = prevAvg * day5Change
amount5Change = round(amount5Change, 8)

print("Latest Open:", prevOpen)
print("Latest Close:", prevClose)
print("Yesterday's Average Price:", prevAvg)
print("Percent Change over 5 days:", day5Change)
print("Price Change over 5 days:", amount5Change)



print()
# Sentiment Score * 5 day Percent Change to account for sentiment score
calculation = sentiment_score * day5Change
print("New 5 day change:", calculation)

#Take the new 5 day Change and * by yesterday's average to account for latest price flucuations
calculation = calculation * prevAvg
calculation = round(calculation,2)
print(calculation)


# Account for + or - sentiment scores to correct the price direction
# If score is +  ==> price goes up
# If score is -  ==> price goes down
print("Amount stock will gain or lose: ", calculation)
if sentiment_score <= 0:
    prediction = (prevAvg) + (-(calculation))
    
else:
    prediction = (prevAvg) + (calculation)

prediction = str(round(prediction, 2))
print("Predicted price: ", prediction)



# We decided to score sentiment by hand -- this was code I planned to use to analyze sentiment

#Load api with wait rate
#api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

#account =input("Enter account @: ")
#account = api.get_user(account)
#print("Twitter user: ", account.screen_name)
#print("Number of followers: ", account.followers_count)

#Collect tweet selected
# Number of tweets to be extracted 
#number_of_tweets=30
#tweets = api.user_timeline(screen_name=account) 
  
# Empty Array 
#tmp=[]  
  
# create array of tweet information: username,  
# tweet id, date/time, text 
#tweets_for_csv = [tweet.text for tweet in tweets] # CSV file created  
#for j in tweets_for_csv: 
  
# Appending tweets to the empty array tmp 
#    tmp.append(j)  
  
# Printing the tweets 
#print()
#print(tmp[0]) 



#Sentiment analysis
#tweetBlob = TextBlob(tmp[0])
#print("Tweet Sentiment: " , tweetBlob.sentiment)


