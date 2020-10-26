
from django.urls import path

from training.views import TrainingSessionDetailView, TrainingSessionCreateView
from .views import home, add_player, PlayerListView, PlayerDetailView, \
    PlayerUpdateView, CoachListView, coach_register, \
    CoachDetailView, CoachUpdateView, CoachDeleteView, \
    contact_us, PlayerDeleteView, ContactUsListView, ContactUsDetailView, ContactUsDeleteView, add_injury, updateInjury, \
    deleteInjury

urlpatterns = [
    path('', home, name='home'),
    path('add_player/', add_player, name='add-player'),
    path('players/', PlayerListView.as_view(), name='player-list'),
    path('players/<int:pk>/', PlayerDetailView.as_view(), name='player-detail'),
    path('players/<int:pk>/update/', PlayerUpdateView.as_view(), name='player-update'),
    path('players/<int:pk>/add_injury/', add_injury, name='add_injury'),
    path('injury/<int:pk>/update_injury/', updateInjury, name='update_injury'),
    path('injury/<int:pk>/delete_injury/', deleteInjury, name='delete_injury'),
    path('players/<int:pk>/delete/', PlayerDeleteView.as_view(), name='player-delete'),

    path('coaches/', CoachListView.as_view(), name='coach-list'),
    path('coach-register/', coach_register, name='coach-register'),
    path('coaches/<int:pk>/', CoachDetailView.as_view(), name='coach-detail'),
    path('coaches/<int:pk>/update', CoachUpdateView.as_view(), name='coach-update'),
    path('coaches/<int:pk>/delete', CoachDeleteView.as_view(), name='coach-delete'),

    path('create-session/', TrainingSessionCreateView.as_view(), name='create-session'),
    path('training/<int:pk>/', TrainingSessionDetailView.as_view(), name='training-detail'),

    path('contact/', contact_us, name='contact-us'),
    path('contact-list/', ContactUsListView.as_view(), name='contact-list'),
    path('contact-list/<int:pk>/', ContactUsDetailView.as_view(), name='contact-detail'),
    path('contact-list/<int:pk>/delete', ContactUsDeleteView.as_view(), name='contact-delete'),

]