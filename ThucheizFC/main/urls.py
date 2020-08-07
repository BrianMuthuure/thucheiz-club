
from django.urls import path

from .views import home, add_player, PlayerListView, PlayerDetailView, PlayerUpdateView, user_login, \
    player_contract_create, CoachListView, coach_register, CoachDetailView, CoachUpdateView, CoachDeleteView, \
    contact_us, PlayerDeleteView

urlpatterns = [
    path('', home, name='home'),
    path('add_player/', add_player, name='add-player'),
    path('create_contract/', player_contract_create, name='create-contract'),
    path('players/', PlayerListView.as_view(), name='player-list'),
    path('players/<int:pk>/', PlayerDetailView.as_view(), name='player-detail'),
    path('players/<int:pk>/update/', PlayerUpdateView.as_view(), name='player-update'),
    path('players/<int:pk>/delete/', PlayerDeleteView.as_view(), name='player-delete'),

    path('coaches/', CoachListView.as_view(), name='coach-list'),
    path('coach-register/', coach_register, name='coach-register'),
    path('coaches/<int:pk>/', CoachDetailView.as_view(), name='coach-detail'),
    path('coaches/<int:pk>/update', CoachUpdateView.as_view(), name='coach-update'),
    path('coaches/<int:pk>/delete', CoachDeleteView.as_view(), name='coach-delete'),
    path('contact/', contact_us, name='contact-us'),
]