from django.conf.urls import url
from django.views.generic.base import RedirectView

from tweets.api.views import (
    TweetListAPIView,
    )

app_name = 'tweet'

urlpatterns = [
    url(r'^(?P<username>[\w.@+-]+)/tweet/$', TweetListAPIView.as_view(), name='list'), #
]