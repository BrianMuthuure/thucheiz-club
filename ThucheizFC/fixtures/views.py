from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from fixtures.models import Fixture


class FixtureListView(ListView):
    model = Fixture
    context_object_name = 'fixtures'
    template_name = 'fixtures/fixture_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super(FixtureListView, self).get_context_data(*args, **kwargs)
        return context


class FixtureDetailView(DetailView):
    model = Fixture
    template_name = 'fixtures/fixture_detail.html'

    def get_context_data(self, **kwargs):
        context = super(FixtureDetailView, self).get_context_data(**kwargs)
        return context

