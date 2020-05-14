from django import forms
from .models import Fetcher

class FetcherCreateForm(forms.ModelForm):
    class Meta:
        model = Fetcher
        fields = ['search_term', 'categories', 'need_filter', 'retweets_of']