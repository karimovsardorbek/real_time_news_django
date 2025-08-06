from django.db import models


# Model representing a news article
class Article(models.Model):
    title = models.CharField(max_length=255)
    summary = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100, default='Anonymous', blank=True, null=True)
    image = models.URLField(blank=True, null=True)

    class Meta:
        ordering = ['-publication_date']

    def __str__(self):
        return self.title