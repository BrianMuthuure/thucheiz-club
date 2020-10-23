from django.urls import path

from results.views import ResultListView, ResultCreateView, ResultDeleteView, \
    ResultUpdateView, ResultDetailView, add_goals

urlpatterns = [
    path('', ResultListView.as_view(), name='result-list'),
    path('<int:pk>/', ResultDetailView.as_view(), name='result-detail'),
    path('create-result/', ResultCreateView.as_view(), name='create_result'),
    path('<int:pk>/add_goals/', add_goals, name='add_goals'),
    path('<int:pk>/update/', ResultUpdateView.as_view(), name='result-update'),
    path('<int:pk>/delete/', ResultDeleteView.as_view(), name='result-delete'),

]