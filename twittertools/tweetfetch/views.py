from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import View

from .models import Fetcher


class IndexView(generic.ListView):
    template_name = 'tweetfetch/index.html'

    def get_queryset(self):
        return

class CommandCreate(CreateView):
    model = Fetcher
    fields = ['search_term', 'categories_list', 'tweet_filter']
