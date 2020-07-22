from django.urls import path

from fixtures.views import FixtureListView, FixtureDetailView, FixtureCreateView, FixtureUpdateView, FixtureDeleteView

urlpatterns = [
    path('', FixtureListView.as_view(), name='fixture-list'),
    path('<int:pk>/', FixtureDetailView.as_view(), name='fixture-detail'),
    path('add/', FixtureCreateView.as_view(), name='fixture-create'),
    path('<int:pk>/update/', FixtureUpdateView.as_view(), name='fixture-update'),
    path('<int:pk>/delete/', FixtureDeleteView.as_view(), name='fixture-delete'),
]