from django.db import models

# Create your models here.
class ClientDataStore(models.Model):
    fullname = models.CharField(max_length=200)
    email = models.CharField(max_length=300)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    def __str__(self):
        return self.username

