import tweepy
import datetime

# Enter your Twitter API keys here
# Consumer Key/Secret = API Key/Secret
consumer_key = 'hG3s3j7UBv7zk1FC2stDty65W'
consumer_secret = 'P2WCPfPn4jtpH8QbofgxJWvR1yboqVKt3SE57e5aM0zEp3kDvc'
access_token = '128944911-Sj0MULowDCRJQQKz6cCNcNyUiwMWUjhs5xh12oL4'
access_token_secret = 'W6EMHMf7J67prz0Tol2QXAvaG8VHBcYFiWxS2gYfhXd22'

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Handle of the account whose tweets you want to like
handle = 'sangilikamesh'

# Time range for tweets (in this case, last 24 hours)
time_range = datetime.datetime.now() - datetime.timedelta(days=1)

# Search for tweets from the specified handle
tweets = api.search(q='from:' + handle)

# Like each tweet
for tweet in tweets:
    # Check if tweet was posted within the time range
    if tweet.created_at > time_range:
        try:
            api.create_favorite(tweet.id)
            print('Liked tweet:', tweet.text)
        except tweepy.TweepError as e:
            print(e)
    else:
        print('Tweet is not within the specified time range')
