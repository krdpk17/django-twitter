from django.db import models
from django.urls import reverse

class Fetcher(models.Model):
    search_term = models.CharField(max_length=250)
    categories_list = models.CharField(max_length=250)
    tweet_filter = models.CharField(max_length = 1000)
    def get_absolute_url(self):
        return reverse("music:detail", kwargs={"pk": self.pk})
    
    def __str__(self):
        return self.search_term + '-' + self.categories_list + '-' + self.tweet_filter