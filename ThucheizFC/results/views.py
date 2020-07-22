from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from results.forms import ResultCreationForm
from results.models import Result


class ResultListView(ListView):
    model = Result
    context_object_name = 'results'
    template_name = 'results/result_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ResultListView, self).get_context_data(*args, **kwargs)
        return context


class ResultDetailView(DetailView):
    model = Result
    template_name = 'results/result_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ResultDetailView, self).get_context_data(**kwargs)
        return context


class ResultCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    model = Result
    form_class = ResultCreationForm
    template_name = 'results/create_result.html'
    success_message = "result has been created successfully"


class ResultUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    model = Result
    template_name = 'results/create_result.html'
    form_class = ResultCreationForm
    success_message = "Result update was successful"


class ResultDeleteView(LoginRequiredMixin, DeleteView):
    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    model = Result
    template_name = 'results/delete_result.html'
    success_url = '/results'
