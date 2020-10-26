from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView, CreateView, UpdateView

from training.models import TrainingSession


class TrainingSessionDetailView(DetailView):
    model = TrainingSession
    context_object_name = 'session'
    template_name = 'training/session_detail.html'

    def get_context_data(self, **kwargs):
        context = super(TrainingSessionDetailView, self).get_context_data(**kwargs)
        return context


class TrainingSessionCreateView(CreateView):
    model = TrainingSession
    fields = '__all__'
    template_name = 'training/add_new_session.html'
    success_url = ('/')


class TrainingSessionUpdateView(UpdateView):
    pass
