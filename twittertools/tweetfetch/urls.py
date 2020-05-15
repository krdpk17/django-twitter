from django.conf.urls import include,url
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

from . import views 
# from django.views.generic import TemplateView

app_name = 'tweetfetch'
urlpatterns = [
	#/tweetfetch/
    url(r'^$', views.IndexView.as_view(), name='index'),
    #/tweetfetch/fetcher/add
    url(r'fetcher/add/$', views.CommandCreate.as_view(), name="fetcher-add"),
    #/tweetfetch/fetcher/list
    url(r'fetcher/list/$', views.CommandList.as_view(), name="fetcher-list"),


]