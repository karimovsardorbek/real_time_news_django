from django.urls import path
from news.views import ArticleListView, GenerateMockArticleView


urlpatterns = [
    path('api/articles/', ArticleListView.as_view(), name='article_list'),
    path('api/generate-news/', GenerateMockArticleView.as_view(), name='generate_news'),
]
