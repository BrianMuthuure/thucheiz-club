from django.urls import path

from fixtures.views import FixtureListView, FixtureDetailView

urlpatterns = [
    path('', FixtureListView.as_view(), name='fixture-list'),
    path('<int:pk>/', FixtureDetailView.as_view(), name='fixture-detail'),
]