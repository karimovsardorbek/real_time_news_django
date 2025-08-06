from django.contrib import admin
from news.models import Article


# Register the Article model with the Django admin site
admin.site.register(Article)