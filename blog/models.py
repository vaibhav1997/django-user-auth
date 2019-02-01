from django.contrib.auth.models import AbstractUser
from django.shortcuts import get_object_or_404 #New
from django.db import models
from django.template.defaultfilters import slugify
from ckeditor_uploader.fields import RichTextUploadingField #New


# Create your models here.
class CustomUser(AbstractUser):

    def __str__(self):
        return self.email

AUTHOR_CHOICES = [
        ('John','John'),
        ('Dev','Dev'),
        ('Amy','Amy'),
        ('Eva','Eva'),
    ]
CATEGORIES = [
    ('Games', 'Games'),
    ('Lifestyle', 'Lifestyle'),
    ('Sports', 'Sports'),
    ('Developer', 'Developer'),
    ('Food', 'Food'),
    ('Travel', 'Travel'),
    ('Movies', 'Movies'),
    ('Photography', 'Photography/Filmography'),
]

class Post(models.Model):
    title = models.CharField(max_length = 100)
    content = RichTextUploadingField()
    
    author = models.CharField(max_length = 50, choices = AUTHOR_CHOICES)
    url = models.SlugField(max_length = 100, unique = True)
    likes = models.PositiveSmallIntegerField(default = 1)
    imageurl = models.CharField(max_length = 150, blank = True)
    uploadimg = models.ImageField(upload_to = 'uploads/%Y/%m/%d/', blank = True)
    category = models.CharField(max_length = 15, choices = CATEGORIES, default = "Not Categorized")
    commentcounter = models.PositiveSmallIntegerField(editable = False, default = 0)

    def get_absolute_url(self):
        return self.url


    def save(self, *args, **kwargs):
        self.url = slugify(self.title)
        super(Post, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.title


class Comment(models.Model):
    comment_text = models.CharField(max_length = 150)
    title = models.ForeignKey(Post, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now = True)

    # def save(self, *args, **kwargs): #New
    #     defTitle = get_object_or_404(Post)
    #     self.title = defTitle.id
    #     super(Comment, self).save(*args, **kwargs)

    def __str__(self):
        return self.comment_text
