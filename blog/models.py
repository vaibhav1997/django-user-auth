from django.contrib.auth.models import AbstractUser
from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class CustomUser(AbstractUser):

    def __str__(self):
        return self.email

class Post(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    author = models.CharField(max_length = 100)
    url = models.SlugField(max_length = 100, unique = True)
    likes = models.PositiveSmallIntegerField(default = 1)
    # imageurl = models.CharField(max_length = 150, default = 1)

    def get_absolute_url(self):
        return self.url


    def save(self, *args, **kwargs):
        self.url = slugify(self.title)
        super(Post, self).save(*args, **kwargs)


# class Comments(models.Model):
