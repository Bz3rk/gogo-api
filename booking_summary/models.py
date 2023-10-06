from django.db import models
from django.contrib.auth.models import User



class BookingSummary (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_location = models.CharField(max_length=300)
    destination = models.CharField(max_length=300)
    two_way = models.BooleanField()
    no_of_passengers = models.IntegerField()
    pickup_long = models.FloatField()
    pickup_lat = models.FloatField()
    dest_long = models.FloatField()
    dest_lat = models.FloatField()
    distance = models.FloatField()
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
   
