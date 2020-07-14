from django.urls import path

from results.views import ResultListView

urlpatterns = [
    path('', ResultListView.as_view(), name='results-list'),
]