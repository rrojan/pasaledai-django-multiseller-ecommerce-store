from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date


class Article(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    slug = models.SlugField(blank=True, null=True)
    featured = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    # thumb = models.ImageField(default='default.png', blank=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT, default=None)

    def get_absolute_url(self):
        return reverse('articles:detail-view', kwargs={"id": self.id})

    def __str__(self):
        return self.title

    def snippet(self):
        return self.description[:70] + '...'