from django.contrib.auth.models import User
from django.db import models
#from ..API.model import ClientRegistration

# Create your models here.




class Testimonials(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class meta:
        ordering = ['-created']

    def __str__(self):
        return self.body[0:30]



