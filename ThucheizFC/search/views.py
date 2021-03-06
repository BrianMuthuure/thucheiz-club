from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from fixtures.models import Fixture
from main.models import Player, Coach
from news.models import News
from results.models import Result


class PlayerSearchView(ListView):
    context_object_name = 'players'
    template_name = 'search/player_search.html'

    def get_context_data(self, *args, **kwargs):
        context = super(PlayerSearchView, self).get_context_data(*args, **kwargs)
        query = self.request.GET.get('q')
        context['query'] = query
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        method_dict = request.GET
        query = method_dict.get('q', None)
        print(query)
        if query is not None:
            return Player.objects.search(query)
        return Player.objects.all()


class CoachSearchView(ListView):
    context_object_name = 'coaches'
    template_name = 'search/coach_search.html'

    def get_context_data(self, *args, **kwargs):
        context = super(CoachSearchView, self).get_context_data(*args, **kwargs)
        query = self.request.GET.get('q')
        context['query'] = query
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        method_dict = request.GET
        query = method_dict.get('q', None)
        print(query)
        if query is not None:
            return Coach.objects.search(query)
        return Coach.objects.none()


class NewsSearchView(ListView):
    context_object_name = 'news'
    template_name = 'search/news_search.html'

    def get_context_data(self, *args, **kwargs):
        context = super(NewsSearchView, self).get_context_data(*args, **kwargs)
        query = self.request.GET.get('q')
        context['query'] = query
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        method_dict = request.GET
        query = method_dict.get('q', None)
        print(query)
        if query is not None:
            return News.objects.search(query)
        return News.objects.none()


class ResultSearchView(ListView):
    context_object_name = 'results'
    template_name = 'search/result_search.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ResultSearchView, self).get_context_data(*args, **kwargs)
        query = self.request.GET.get('q')
        context['query'] = query
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        method_dict = request.GET
        query = method_dict.get('q', None)
        print(query)
        if query is not None:
            return Result.objects.search(query)
        return Result.objects.none()


class FixtureSearchView(ListView):
    context_object_name = 'fixtures'
    template_name = 'search/fixture_search.html'

    def get_context_data(self, *args, **kwargs):
        context = super(FixtureSearchView, self).get_context_data(*args, **kwargs)
        query = self.request.GET.get('q')
        context['query'] = query
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        method_dict = request.GET
        query = method_dict.get('q', None)
        print(query)
        if query is not None:
            return Fixture.objects.search(query)
        return Fixture.objects.none()