from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Profile(models.Model):
    address=models.TextField()
    profile_pic=models.ImageField()
    username=models.OneToOneField(User,on_delete=models.CASCADE)