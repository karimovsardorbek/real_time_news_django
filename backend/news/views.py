from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Article
from .serializers import ArticleSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from faker import Faker
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
import random


# View to retrieve a list of articles
class ArticleListView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        articles = Article.objects.all().order_by('-id')
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)


# View to generate a mock article
class GenerateMockArticleView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        fake = Faker()
        random_image_url = f"https://picsum.photos/seed/{random.randint(1, 10000)}/600/400"
        article = Article.objects.create(
            title=fake.sentence(),
            summary=fake.paragraph(nb_sentences=10),
            author=fake.name() if random.choice([True, False]) else None,
            image=random_image_url
        )

        serializer = ArticleSerializer(article)

        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            'news',
            {
                'type': 'send_article',
                'article': serializer.data,
            }
        )
        return Response(serializer.data)