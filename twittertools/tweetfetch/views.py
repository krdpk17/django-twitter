from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View

from .models import Fetcher
from .forms import UserForm


class IndexView(generic.ListView):
    template_name = 'tweetfetch/index.html'

    def get_queryset(self):
        return

class CommandCreate(CreateView):
    model = Fetcher
    fields = ['search_term', 'categories_list', 'tweet_filter']

class UserFormView(View):
    form_class = UserForm
    template_name = 'tweetfetch/registration_form.html'

    #Display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    #Process form data
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            # Cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # Returns User objects if credential are correct
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('tweetfetch:index')
                    
        return render(request, self.template_name, {'form': form})
