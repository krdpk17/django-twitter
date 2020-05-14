from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib import messages

from .forms import FetcherCreateForm


class IndexView(generic.ListView):
    template_name = 'tweetfetch/index.html'

    def get_queryset(self):
        return

class CommandCreate(CreateView):
    form_class = FetcherCreateForm
    success_url = reverse_lazy('tweetsfetch:index')
    template_name = 'tweetfetch/fetcher_form.html'

    def get(self, request):
        form = self.form_class(None)
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.POST)
        context = {'form': form}
        #TODO: Store this info in the Database
        messages.success(request, 'TBD')
        return render(request, self.template_name, context)