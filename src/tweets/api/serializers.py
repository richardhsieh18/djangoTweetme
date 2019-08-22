from django.utils.timesince import timesince
from rest_framework import serializers

from accounts.api.serializers import UserDisplaySerializer
from tweets.models import Tweet

class ParentTweetModelSerialzer(serializers.ModelSerializer):
    user = UserDisplaySerializer(read_only=True)
    date_display = serializers.SerializerMethodField()
    timesince = serializers.SerializerMethodField()

    class Meta:
        model = Tweet
        fields = [
            'id',
            'user',
            'content',
            'timestamp',
            'date_display',
            'timesince',
        ]


    def get_date_display(self, obj):
        return obj.timestamp.strftime("%b %d %Y, %I:%M %p")

    def get_timesince(self, obj):
        return timesince(obj.timestamp) + "ago"

class TweetModelSerialzer(serializers.ModelSerializer):
    user = UserDisplaySerializer(read_only=True)
    date_display = serializers.SerializerMethodField()
    timesince = serializers.SerializerMethodField()
    parent = ParentTweetModelSerialzer(read_only=True)
    
    class Meta:
        model = Tweet
        fields = [
            'id',
            'user',
            'content',
            'timestamp',
            'date_display',
            'timesince',
            'parent',
        ]

    def get_date_display(self, obj):
        return obj.timestamp.strftime("%b %d %Y, %I:%M %p")

    def get_timesince(self, obj):
        return timesince(obj.timestamp) + "ago"