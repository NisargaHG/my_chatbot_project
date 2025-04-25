import tweepy

def authenticate_twitter():
    """Authenticate with Twitter API and return a Tweepy client."""
    api_key = "4tTDvbT3tkL7m6ab1Lop6xhYO"
    api_secret = "zcn1iQJj6GRmJuzlYADkWgtXzGFakkewPeZguqB3867tr29uXE"
    access_token = "1884503973530591232-55lP5zJI27peAGQKvHxvtpUEZrQTty"
    access_token_secret = "a4Qrh8Cah7uu17hU39JEm88fvai1tzMuaHr44yAiXmqiC"
    bearer_token = "AAAAAAAAAAAAAAAAAAAAABhGygEAAAAAON9i4i2lfNqSv%2FJdRQNJXIFCvnQ%3DgrxuWMEP0qqdznCGIV4QnGaTfQQoQvtMRRFT1bOhuNng4MZNW5"


    try:
        client = tweepy.Client(
            consumer_key=api_key,
            consumer_secret=api_secret,
            access_token=access_token,
            access_token_secret=access_token_secret,
            bearer_token=bearer_token
        )
        return client
    except Exception as e:
        print(f"Twitter authentication failed: {e}")
        return None
