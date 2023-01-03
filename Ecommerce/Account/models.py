from django.db import models
from django.contrib.auth.models import User
from Home.models import Products
# Create your models here.

class UserModel(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    phone = models.IntegerField(null=True)
    prod = models.ManyToManyField(Products)

    def __str__(self) -> str:
        return self.user.username