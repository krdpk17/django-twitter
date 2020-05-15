import django_tables2 as tables
from .models import Fetcher

class FetcherTable(tables.Table):
    class Meta:
        model = Fetcher
        fields = ['id', 'search_term','state', 'need_filter']