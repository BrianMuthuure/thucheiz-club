from django.urls import path

from news.views import NewsListView, NewsCreateView, NewsDetailView, NewsUpdateView, NewsDeleteView

urlpatterns = [
    path('', NewsListView.as_view(), name='news-list'),
    path('<int:pk>/', NewsDetailView.as_view(), name='news-detail'),
    path('<int:pk>/update', NewsUpdateView.as_view(), name='news-update'),
    path('create_news/', NewsCreateView.as_view(), name='news-create'),
    path('<int:pk>/delete', NewsDeleteView.as_view(), name='news-delete'),

]