from django.db import models

class Restaurant(models.Model):
    name=models.CharField(max_length=255,default="Restaurant")
    description=models.CharField(max_length=500,null=True)
    lng=models.FloatField()
    lat=models.FloatField()
    created_at=models.DateTimeField(auto_now_add=True,null=True)
    updated_date=models.DateTimeField(auto_now=True)
    
    owner = models.ForeignKey('authentification.User', related_name='restaurants', on_delete=models.CASCADE,null=True)


    def __str__(self):
        return self.name