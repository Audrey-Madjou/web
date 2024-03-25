from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User_connect(AbstractUser) :
    CREATOR = 'CREATOR'
    SUBSCRIBER = 'SUBSCRIBER'
    ROLE_CHOICES = {
        (CREATOR,'Creator'),
        (SUBSCRIBER,'Subscriber')
    }
    ROLES = models.CharField(max_length = 20,choices= ROLE_CHOICES,verbose_name='Role')
    user_photo = models.ImageField(verbose_name='photo de profil')
