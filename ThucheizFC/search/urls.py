from django.urls import path

from search.views import PlayerSearchView, CoachSearchView, NewsSearchView

urlpatterns = [
    path('', PlayerSearchView.as_view(), name='query'),
    path('coach/', CoachSearchView.as_view(), name='coach_query'),
    path('news/', NewsSearchView.as_view(), name='news_query'),
]