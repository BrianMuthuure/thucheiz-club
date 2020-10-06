from django.urls import path

from results.views import ResultListView, ResultDetailView, add_goals, ResultCreateView, ResultDeleteView, \
    ResultUpdateView

urlpatterns = [
    path('', ResultListView.as_view(), name='result-list'),
    path('<int:pk>/', ResultDetailView.as_view(), name='result-detail'),
    path('create-goal/', add_goals, name='add_goals'),
    path('create-result/', ResultCreateView.as_view(), name='create_result'),
    path('<int:pk>/update/', ResultUpdateView.as_view(), name='result-update'),
    path('<int:pk>/delete/', ResultDeleteView.as_view(), name='result-delete'),

]