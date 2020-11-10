from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from training.forms import TrainingForm
from training.models import TrainingSession


class TrainingSessionDetailView(LoginRequiredMixin, DetailView):
    model = TrainingSession
    context_object_name = 'session'
    template_name = 'training/session_detail.html'

    def get_context_data(self, **kwargs):
        context = super(TrainingSessionDetailView, self).get_context_data(**kwargs)
        return context


class TrainingSessionCreateView(LoginRequiredMixin, CreateView):
    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    model = TrainingSession
    form_class = TrainingForm
    template_name = 'training/add_new_session.html'
    success_url = ('/')


class TrainingSessionUpdateView(LoginRequiredMixin, UpdateView):
    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    model = TrainingSession
    fields = '__all__'
    template_name = 'training/add_new_session.html'


class TrainingSessionDeleteView(LoginRequiredMixin, DeleteView):
    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    model = TrainingSession
    template_name = 'training/delete_session.html'
    success_url = '/'
