import random
import tweepy
import time

# Create a list of quotes
quotes = [
   
   #add quotes ....
]

# Create an empty list to store tweeted quotes
tweeted_quotes = []

# Function that returns a random quote
def get_quote():
    # If all quotes have been tweeted, reset the list of tweeted quotes
    if len(tweeted_quotes) == len(quotes):
        tweeted_quotes.clear()
    
    # Select a random quote that hasn't been tweeted yet
    quote = random.choice(quotes)
    while quote in tweeted_quotes:
        quote = random.choice(quotes)
    
    # Add the quote to the list of tweeted quotes
    tweeted_quotes.append(quote)
    
    return quote

# Authenticate your app and create an API client
api_key = "YOUR_API_KEY"
api_secret = "YOUR_API_SECRET"

auth = tweepy.OAuth1UserHandler(api_key, api_secret)
api = tweepy.API(auth)

# Tweet a random quote every 12 hours
while True:
    quote = get_quote()
    api.update_status(quote)
    time.sleep(43200)  # 12 hours in seconds