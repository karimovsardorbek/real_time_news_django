from rest_framework import serializers
from news.models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'summary', 'publication_date', 'author', 'image']
