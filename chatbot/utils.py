import logging
from tweepy import Client
from chatbot.auth import authenticate_twitter  

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.ERROR, format="%(asctime)s - %(levelname)s - %(message)s")

def get_tweets(query, max_results=10):
    """Fetch recent tweets based on a user's query with better filtering"""
    try:
        client = authenticate_twitter()
        if not client:
            return {"status": "error", "message": "Twitter authentication failed."}

        response = client.search_recent_tweets(
            query=f"{query} -is:retweet",  
            max_results=max_results,
            tweet_fields=["created_at", "source", "author_id"]
        )

        if not response.data:
            return {"status": "success", "query": query, "tweets": []}

        tweets_list = []
        for tweet in response.data:
            if query.lower() in tweet.text.lower():  
                tweets_list.append({
                    "text": tweet.text,
                    "author": tweet.author_id,
                    "source": tweet.source if hasattr(tweet, "source") else "Unknown",
                    "time": tweet.created_at.isoformat() if hasattr(tweet, "created_at") else "Unknown"
                })

        return {"status": "success", "query": query, "tweets": tweets_list}

    except Exception as e:
        logger.error(f"Unexpected error: {e}")  
        return {"status": "error", "message": str(e)}
