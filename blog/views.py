from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from .models import Post
from django.http import HttpResponse, HttpResponseRedirect

from .forms import CustomUserCreationForm, AddPost
# Create your views here.

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def post(request):
    if request.method == 'POST':
        form = AddPost(request.POST)
        if form.is_valid():
            form.save()
            return redirect('http://127.0.0.1:8000')
    else:
        form = AddPost()

    return render(request, 'blog.html', {'blog_form': form })

def display(request):
    blogs = Post.objects.all()
    return render(request, 'home.html', {'blogpost': blogs})

def detailView(request, slug):
    blogs = get_object_or_404(Post, url = slug)
    return render(request, 'viewpost.html', {'post': blogs})