from rest_framework import serializers
from .models import BookingSummary


class BookingSummarySerializer (serializers.ModelSerializer):
    distance = serializers.FloatField(read_only=True)
    price = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = BookingSummary
        fields = ['user', 'user_location', 'destination', 'two_way', 'no_of_passengers', 'pickup_long', 'pickup_lat', 'dest_long', 'dest_lat', 'distance', 'price']