import tweepy
import requests
import os
import tweepy.api
import tweepy.client

consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")


client = tweepy.Client(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)



auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


response = requests.get('https://api.sefinek.net/api/v2/random/animal/cat')
data = response.json()

# print(data) just for debugging lol

if 'message' in data:
    image_url = data['message']

image_response = requests.get(image_url)
with open('cat.jpg', 'wb') as file:
    file.write(image_response.content)

media = api.simple_upload(filename='cat.jpg')
tweepy.Client.create_tweet(text="Here's your daily cat!!", media_ids=[media.media_id], self= client)

os.remove('cat.jpg')