from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

class CustomUser(AbstractUser):
    parent = models.ForeignKey('self', blank=True,null=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.username