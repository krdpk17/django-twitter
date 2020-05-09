from django.conf.urls import include,url
from . import views 
# from django.views.generic import TemplateView

app_name = 'tweetfetch'
urlpatterns = [
	#/tweetfetch/
    url(r'^$', views.IndexView.as_view(), name='index'),

    # url(r'^$', TemplateView.as_view(template_name="about.html")),
]