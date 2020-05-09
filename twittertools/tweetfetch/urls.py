from django.conf.urls import include,url
from . import views 
# from django.views.generic import TemplateView

app_name = 'tweetfetch'
urlpatterns = [
	#/tweetfetch/
    url(r'^$', views.IndexView.as_view(), name='index'),

    url(r'^register/$', views.UserFormView.as_view(), name='register'),

    #/tweetfetch/fetcher/add
    url(r'fetcher/add/$', views.CommandCreate.as_view(), name="fetcher-add"),


]