from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import View, ListView
from django.contrib import messages

from .forms import FetcherCreateForm
from .fetcher_db_intf import store_fetch_query, fetch_all_queries_by_user
from .models import Fetcher
from .tables import FetcherTable

class IndexView(generic.ListView):
    template_name = 'tweetfetch/index.html'

    def get_queryset(self):
        return

class CommandList(ListView):
    template_name = 'table_template.html'
    fetcher_table = FetcherTable

    def get(self, request):
        queries = fetch_all_queries_by_user(request.user)
        table = self.fetcher_table(queries)
        #istekler = queries.all()

        return render(request, self.template_name, locals())
    
    def post(self, request):
        pass

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
        #Store this info in the Database
        status = store_fetch_query(form.data, request.user)
        if status:
            messages.success(request, 'Stored query in the DB')
            return redirect('tweetfetch:index')
        else:
            messages.error(request, 'Failed to store query. Please retry')
            return render(request, self.template_name, context)