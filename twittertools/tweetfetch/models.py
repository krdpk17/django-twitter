from django.db import models
from django.urls import reverse

class Fetcher(models.Model):
    search_term = models.CharField(max_length=250)
    categories = models.CharField(max_length=250)
    need_filter = models.BooleanField(blank=True, default=False)
    retweets_of = models.CharField(max_length = 200, blank=True)
    def get_absolute_url(self):
        return reverse("tweetfetch:index")
    
    # def __str__(self):
    #     return self.search_term + '-' + self.categories_list + '-' + self.tweet_filter