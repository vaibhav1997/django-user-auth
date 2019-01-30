from django.contrib.auth.models import AbstractUser
from django.db import models
from django.template.defaultfilters import slugify
from ckeditor_uploader.fields import RichTextUploadingField #New


# Create your models here.
class CustomUser(AbstractUser):

    def __str__(self):
        return self.email

class Post(models.Model):
    title = models.CharField(max_length = 100)
    content = RichTextUploadingField()
    AUTHOR_CHOICES = [
        ('John','John'),
        ('Dev','Dev'),
        ('Amy','Amy'),
        ('Eva','Eva'),
    ]
    author = models.CharField(max_length = 50, choices = AUTHOR_CHOICES)
    url = models.SlugField(max_length = 100, unique = True)
    likes = models.PositiveSmallIntegerField(default = 1)
    imageurl = models.CharField(max_length = 150, blank = True)

    def get_absolute_url(self):
        return self.url


    def save(self, *args, **kwargs):
        self.url = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

# class CkModel(models.Model):  #New
#     content = RichTextUploadingField()
# class Comments(models.Model):
