
from django.urls import path

from training.views import TrainingSessionDetailView, \
    TrainingSessionCreateView, TrainingSessionUpdateView, \
    TrainingSessionDeleteView, TrainingSessionListView, training_list
from .views import home, add_player, PlayerListView, \
    PlayerDetailView, PlayerUpdateView, CoachListView, \
    coach_register, CoachDetailView, CoachUpdateView, \
    CoachDeleteView, contact_us, PlayerDeleteView, \
    ContactUsListView, ContactUsDetailView, ContactUsDeleteView, \
    add_injury, updateInjury, deleteInjury, inaccessible_player, \
    inaccessible_players_listview, export_csv, export_excel, Pdf, \
    injury_list, ContractUpdateView, InjuryPdf, add_jersey, delete_inaccessible, contract_list, \
    inaccessible_players_detailview, ContractDetailView

urlpatterns = [
    path('', home, name='home'),
    path('add_player/', add_player, name='add-player'),
    path('players/', PlayerListView.as_view(), name='player-list'),
    path('players/<int:pk>/', PlayerDetailView.as_view(), name='player-detail'),
    path('players/<int:pk>/update/', PlayerUpdateView.as_view(), name='player-update'),
    path('players/<int:pk>/delete/', PlayerDeleteView.as_view(), name='player-delete'),

    path('players/<int:pk>/add_inaccessible_player/', inaccessible_player, name='add_unavailable_player'),
    path('inaccessible-players', inaccessible_players_listview, name='unavailable-players'),
    path('inaccessible-players/<int:pk>/', inaccessible_players_detailview, name='inaccessible-detail'),
    path('inaccessible-players/<int:pk>/delete/', delete_inaccessible, name='inaccessible-delete'),


    path('render/pdf/', Pdf.as_view(), name='export-pdf'),
    path('export-csv', export_csv, name='export-csv'),
    path('export-excel', export_excel, name='export-excel'),

    path('contracts/', contract_list, name='contracts'),
    path('contracts/<int:pk>/', ContractDetailView.as_view(), name='contract-detail'),
    path('contracts/<int:pk>/update', ContractUpdateView.as_view(), name='contract-update'),

    path('injury-list/', injury_list, name='injury-list'),
    path('players/<int:pk>/add_injury', add_injury, name='add_injury'),
    path('injury/<int:pk>/update_injury/', updateInjury, name='update_injury'),
    path('injury/<int:pk>/delete_injury/', deleteInjury, name='delete_injury'),
    path('render-injury/pdf/', InjuryPdf.as_view(), name='injury-pdf'),

    path('coaches/', CoachListView.as_view(), name='coach-list'),
    path('coach-register/', coach_register, name='coach-register'),
    path('coaches/<int:pk>/', CoachDetailView.as_view(), name='coach-detail'),
    path('coaches/<int:pk>/update', CoachUpdateView.as_view(), name='coach-update'),
    path('coaches/<int:pk>/delete', CoachDeleteView.as_view(), name='coach-delete'),

    path('sessions/', training_list, name='session-list'),
    path('create-session/', TrainingSessionCreateView.as_view(), name='create-session'),
    path('training/<int:pk>/', TrainingSessionDetailView.as_view(), name='training-detail'),
    path('training/<int:pk>/update', TrainingSessionUpdateView.as_view(), name='training-update'),
    path('training/<int:pk>/delete', TrainingSessionDeleteView.as_view(), name='training-delete'),

    path('contact/', contact_us, name='contact-us'),
    path('contact-list/', ContactUsListView.as_view(), name='contact-list'),
    path('contact-list/<int:pk>/', ContactUsDetailView.as_view(), name='contact-detail'),
    path('contact-list/<int:pk>/delete', ContactUsDeleteView.as_view(), name='contact-delete'),

    path('add-jersey/', add_jersey, name='add-jersey'),

]