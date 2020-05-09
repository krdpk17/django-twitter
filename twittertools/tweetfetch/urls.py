from django.conf.urls import include,url
from django.contrib.auth.views import LoginView

from . import views 
# from django.views.generic import TemplateView

app_name = 'tweetfetch'
urlpatterns = [
	#/tweetfetch/
    url(r'^$', views.IndexView.as_view(), name='index'),

    url(r'^register/$', views.UserFormView.as_view(), name='register'),

    url(r'^login/$', LoginView.as_view()),

    #/tweetfetch/fetcher/add
    url(r'fetcher/add/$', views.CommandCreate.as_view(), name="fetcher-add"),


]