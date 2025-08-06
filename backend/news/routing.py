from django.urls import path
from .consumers import NewsConsumer


# WebSocket URL patterns for the NewsConsumer
websocket_urlpatterns = [
    path('ws/news/', NewsConsumer.as_asgi()),
]
