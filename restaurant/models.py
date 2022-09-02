from django.db import models
from django.conf import settings
from  authentification.models import User
#from django.contrib.auth.models import User 

class Restaurant(models.Model):
    name=models.CharField(max_length=255,default="Restaurant")
    description=models.CharField(max_length=500,null=True)
    lng=models.FloatField()
    lat=models.FloatField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
   
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='restaurants', on_delete=models.CASCADE)

    def __str__(self):
        return self.name