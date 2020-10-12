
from django.urls import path

from injury.views import InjuryListView, add_injury, InjuryDeleteView

urlpatterns = [
    path('add-injury/', add_injury, name='injury_create'),
    path('injuries/', InjuryListView.as_view(), name='injury_list'),
    path('<int:pk>/delete/', InjuryDeleteView.as_view(), name='injury-delete'),
]