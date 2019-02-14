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

class AddPost(ModelForm):
   
    class Meta:
        model = Post
        content = forms.CharField(widget = CKEditorUploadingWidget())
        # author = forms.CharField(widget = forms.Select(choices = AUTHOR_CHOICES))
        model = Post
        fields = ('title', 'content', 'author','imageurl', 'uploadimg', 'category', 'tags') #add 'imageurl'
        REQUIRED_FIELDS = ['title', 'content', 'author']


class EditPost(ModelForm):

    class Meta:
        model = Post
        content = forms.CharField(widget = CKEditorUploadingWidget())
        model = Post
        fields = ('title', 'content', 'author','imageurl', 'uploadimg', 'category') #add 'imageurl'
    def __init__(self, *args, **kwargs):
        super(EditPost, self).__init__(*args, **kwargs)
        uneditable_fields = ['title']
        for field in uneditable_fields:
            self.fields[field].widget.attrs['readonly'] = 'true'
