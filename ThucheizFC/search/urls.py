from django.urls import path

from search.views import PlayerSearchView, CoachSearchView, NewsSearchView, ResultSearchView, FixtureSearchView

urlpatterns = [
    path('', PlayerSearchView.as_view(), name='query'),
    path('coach/', CoachSearchView.as_view(), name='coach_query'),
    path('news/', NewsSearchView.as_view(), name='news_query'),
    path('results/', ResultSearchView.as_view(), name='result_query'),
    path('fixtures/', FixtureSearchView.as_view(), name='fixture_query'),
]