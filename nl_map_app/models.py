# from django.db import models
from django.contrib.gis.db import models
from django.contrib.auth.models import AbstractUser 



# Users model
class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    
    
    def __str__(self):
        return self.email



class Municipalities(models.Model):
    name = models.CharField(max_length = 50)
    location = models.MultiPolygonField(srid=4326)
    objects = models.Manager()
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Municipalities"
        
        
        
