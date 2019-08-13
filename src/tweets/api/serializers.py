from rest_framework import serializers

from accounts.api.serializers import UserDisplaySerializer
from tweets.models import Tweet

class TweetModelSerialzer(serializers.ModelSerializer):
    user = UserDisplaySerializer()
    class Meta:
        model = Tweet
        fields = [
            'user',
            'content'
        ]