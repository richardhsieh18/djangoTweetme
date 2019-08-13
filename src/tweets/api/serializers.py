from rest_framework import serializers

from tweets.models import Tweet

class TweetModelSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = [
            'user',
            'content'
        ]