from rest_framework import generics

from tweets.models import Tweet
from .serializers import TweetModelSerialzer

class TweetListAPIView(generics.ListAPIView):
    serializer_class = TweetModelSerialzer

    def get_queryset(self):
        return Tweet.objects.all()
    