from rest_framework import serializers
from .models import BookingSummary


class BookingSummarySerializer (serializers.ModelSerializer):     
    user = serializers.PrimaryKeyRelatedField(default=serializers.CurrentUserDefault(), read_only=True)
    distance = serializers.FloatField(read_only=True)
    price = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = BookingSummary
        fields = '__all__'