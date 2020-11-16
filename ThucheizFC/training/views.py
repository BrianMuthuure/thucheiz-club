from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView

from main.filters import SessionFilter
from training.forms import TrainingForm
from training.models import TrainingSession


class TrainingSessionListView(ListView):
    model = TrainingSession
    context_object_name = 'sessions'
    template_name = 'training/session_list.html'

    def get_queryset(self):
        qs = self.model.objects.all()
        session_filtered_list = SessionFilter(self.request.GET, queryset=qs)
        return session_filtered_list.qs


def training_list(request):
    sessions =TrainingSession.objects.all().order_by('-date')

    sessionFilter = SessionFilter(request.GET, queryset=sessions)
    sessions = sessionFilter.qs

    page = request.GET.get('page', 1)
    paginator = Paginator(sessions, 5)
    try:
        sessions = paginator.page(page)
    except PageNotAnInteger:
        sessions = paginator.page(1)
    except EmptyPage:
        sessions = paginator.page(paginator.num_pages)
    context = {
        'sessions': sessions,
        'sessionFilter': sessionFilter
    }
    return render(request, 'training/session_list.html', context)


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
    success_url = reverse_lazy('session-list')


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
