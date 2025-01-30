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

def chatbot_ui(request):
    """Render chatbot UI page."""
    return render(request, "chatbot/chatbot.html")
