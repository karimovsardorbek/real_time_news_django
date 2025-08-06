import json
from channels.generic.websocket import AsyncWebsocketConsumer


# Consumer for handling WebSocket connections for news articles
class NewsConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add('news', self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard('news', self.channel_name)

    async def send_article(self, event):
        await self.send(text_data=json.dumps(event['article']))