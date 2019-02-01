from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Post, Comment
from django.forms import ModelForm
# from ckeditor.fields import RichTextUploadingFormField #New
from ckeditor_uploader.widgets import CKEditorUploadingWidget


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

# AUTHOR_CHOICES = [
#             ('John','John'),
#             ('Dev','Dev'),
#             ('Amy','Amy'),
#             ('Eva','Eva'),
#         ]

class AddPost(ModelForm):
   
    class Meta:
        model = Post
        content = forms.CharField(widget = CKEditorUploadingWidget())
        # imageurl = forms.CharField(label = 'Insert URL to display in homepage')
        # author = forms.CharField(widget = forms.Select(choices = AUTHOR_CHOICES))
        model = Post
        fields = ('title', 'content', 'author','imageurl', 'category') #add 'imageurl'
        REQUIRED_FIELDS = ['title', 'content', 'author']

# class CkEditorForm(forms.Form): #New
#     content = RichTextUploadingFormField()



# class PostComment(ModelForm):

#     class Meta:
#         model = Comment
#         fields = ( 'comment_text',)  #Add Title
        