from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from news.forms import NewsCreationForm
from news.models import News


class NewsListView(ListView):
    model = News
    context_object_name = 'news'
    template_name = 'news/news_list.html'
    paginate_by = 6
    ordering = ['-date']

    def get_context_data(self, *args, **kwargs):
        context = super(NewsListView, self).get_context_data(*args, **kwargs)
        return context


class NewsDetailView(DetailView):
    model = News
    template_name = 'news/news_detail.html'

    def get_context_data(self, **kwargs):
        context = super(NewsDetailView, self).get_context_data(**kwargs)
        return context


class NewsCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    model = News
    form_class = NewsCreationForm
    template_name = 'news/create_news.html'
    success_message = "News was created successfully"


class NewsUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    model = News
    template_name = 'news/create_news.html'
    fields = ['title', 'content', 'image']
    success_message = "News was changed successfully "


class NewsDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    model = News
    template_name = 'news/news_delete.html'
    success_url = '/news'
    
    def delete(self, request, *args, **kwargs):
        news = self.get_object()
        messages.success(request, 'News %s was deleted with success!' % news.title)
        return super(NewsDeleteView, self).delete(request, *args, **kwargs)