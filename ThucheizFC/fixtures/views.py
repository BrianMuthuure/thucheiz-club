from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from fixtures.forms import FixtureCreationForm, FixtureUpdateForm
from fixtures.models import Fixture


class FixtureListView(ListView):
    model = Fixture
    context_object_name = 'fixtures'
    template_name = 'fixtures/fixture_list.html'
    paginate_by = 3

    def get_context_data(self, *args, **kwargs):
        context = super(FixtureListView, self).get_context_data(*args, **kwargs)
        return context


class FixtureDetailView(DetailView):
    model = Fixture
    template_name = 'fixtures/fixture_detail.html'

    def get_context_data(self, **kwargs):
        context = super(FixtureDetailView, self).get_context_data(**kwargs)
        return context


class FixtureCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    model = Fixture
    form_class = FixtureCreationForm
    template_name = "fixtures/fixture_create.html"
    success_message = "fixture has been created successfully"


class FixtureUpdateView(SuccessMessageMixin, UpdateView):
    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    model = Fixture
    template_name = 'fixtures/fixture_create.html'
    form_class = FixtureUpdateForm
    success_message = "fixture update was successful"


class FixtureDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    model = Fixture
    template_name = 'fixtures/fixture_delete.html'
    success_message = "Fixture deleted successfully"
    success_url = '/fixtures'