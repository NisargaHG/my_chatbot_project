from django.urls import path
from .views import chatbot_ui, chatbot_response

urlpatterns = [
    path("", chatbot_ui, name="chatbot-ui"),  
    path("api/", chatbot_response, name="chatbot-response"),  
]
