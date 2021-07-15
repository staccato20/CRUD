from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

# Create your models here.


#사용자정보
class UserInformation(models.Model):
    age = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=50, null=True, blank=True)

class CustomUser(AbstractUser):
    age = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=50, null=True, blank=True)