from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):

    def __str__(self):
        return self.email

# class Post(models.Model):
#     title = models.CharField(max_length = 100)
#     content = models.TextField()
#     author = models.CharField(max_length = 100)