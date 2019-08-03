
from django.urls import path
from .views import tweet_detail_view, tweet_list_view, TweetListView, TweetDetailView

urlpatterns = [
    path('', TweetListView.as_view(), name='list'),
    path('2', TweetDetailView.as_view(), name='detail'),

]