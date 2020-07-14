from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from results.models import Result


class ResultListView(ListView):
    model = Result
    context_object_name = 'results'
    template_name = 'results/result_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ResultListView, self).get_context_data(*args, **kwargs)
        return context