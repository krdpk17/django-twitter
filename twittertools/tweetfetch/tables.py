import django_tables2 as tables
from .models import Fetcher

class FetcherTable(tables.Table):
    class Meta:
        model = Fetcher
        fields = ['id', 'categories_list', 'search_term','edit_datetime', 'state',  'type', 'need_filter', 'retweets_of']