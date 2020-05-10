from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic.edit import UpdateView 

from .forms import SignUpForm, ProfileChangeForm

class UpdateProfile(UpdateView):
    success_url = reverse_lazy('tweetfetch:index')
    template_name = 'account_update.html'
    form_class = ProfileChangeForm

    # get current user object
    def get_object(self, queryset=None): 
        return self.request.user

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
    form_class = SignUpForm

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
            password = form.cleaned_data['password1']
            user.set_password(password)
            user.save()

            # Returns User objects if credential are correct
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('tweetfetch:index')
                    
        return render(request, self.template_name, {'form': form})
