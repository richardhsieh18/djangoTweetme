
from django.conf.urls import url
from .views import TweetListView, TweetDetailView

urlpatterns = [
    url(r'^$', TweetListView.as_view(), name='list'),
    #url(r'^(?P<pk>\d+)/$', tweet_detail_view, name="detail"),
    url(r'^(?P<pk>\d+)/$', TweetDetailView.as_view(), name="detail"),

]