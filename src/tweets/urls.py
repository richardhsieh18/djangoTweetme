
from django.urls import path
from .views import tweet_detail_view, tweet_list_view

urlpatterns = [
    path('', tweet_list_view, name='list'),
    path('2', tweet_detail_view, name='detail'),

]