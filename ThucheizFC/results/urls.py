from django.urls import path

from results.views import ResultListView, ResultDetailView, ResultCreateView, ResultUpdateView, ResultDeleteView

urlpatterns = [
    path('', ResultListView.as_view(), name='results-list'),
    path('<int:pk>/', ResultDetailView.as_view(), name='result-detail'),
    path('<int:pk>/update/', ResultUpdateView.as_view(), name='result-update'),
    path('<int:pk>/delete/', ResultDeleteView.as_view(), name='result-delete'),
    path('add/', ResultCreateView.as_view(), name='result-create'),
]