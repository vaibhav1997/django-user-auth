from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Post
from django.forms import ModelForm

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username','email', 'first_name',)
        REQUIRED_FIELDS = ['email']

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')
        REQUIRED_FIELDS = ['email', 'first_name']

class AddPost(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'author','imageurl',) #add 'imageurl'
        REQUIRED_FIELDS = ['title', 'content', 'author']