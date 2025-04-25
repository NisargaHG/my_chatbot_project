from django.shortcuts import render
from django.http import JsonResponse
from .utils import get_tweets

def chatbot_response(request):
    """Handle API request for chatbot responses."""
    if request.method == "GET" and "query" in request.GET:
        query = request.GET.get("query")
        tweets = get_tweets(query)
        return JsonResponse({"tweets": tweets})

    
    return JsonResponse({"error": "Invalid request"}, status=400)

import tweepy
from django.shortcuts import render

def chatbot_ui(request):
    query = request.GET.get('q', '')  # get the query from URL param
    tweets = []

    if query:
        # Twitter API Bearer Token
        bearer_token = "AAAAAAAAAAAAAAAAAAAAABhGygEAAAAAON9i4i2lfNqSv%2FJdRQNJXIFCvnQ%3DgrxuWMEP0qqdznCGIV4QnGaTfQQoQvtMRRFT1bOhuNng4MZNW5"

        client = tweepy.Client(bearer_token=bearer_token)

        # Search recent tweets
        response = client.search_recent_tweets(query=query, max_results=10)

        tweets = [tweet.text for tweet in response.data] if response.data else []

    return render(request, 'chatbot/chatbot.html', {'tweets': tweets, 'query': query})
