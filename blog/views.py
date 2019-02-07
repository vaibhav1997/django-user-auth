from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.urls import reverse_lazy
from django.views import generic
from .models import Post, Comment
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required  #Use only when page view (True) for login
from .forms import CustomUserCreationForm, AddPost, EditPost 
# Create your views here.

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

@login_required
def post(request):
    if request.method == 'POST':
        form = AddPost(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('http://127.0.0.1:8000')
    else:
        form = AddPost()

    return render(request, 'blog.html', {'blog_form': form })

def editpost(request, post_id):
    edpost = get_object_or_404(Post, pk = post_id)
    if request.method == 'POST':
        form = EditPost(request.POST or None, instance = edpost)
        if form.is_valid():
            edit = form.save(commit = False)
            edit.save(update_fields=["content","imageurl","uploadimg"])
            return redirect('http://127.0.0.1:8000')
    else:
        form = EditPost(request.POST or None, instance = edpost)

    return render(request, 'edit.html', {'blog_form': form, 'post':edpost })

def display(request):
    blogs = Post.objects.all()
    # blogcount = get_object_or_404(Post)
    # comment_counter = Comment.objects.filter(title = blogcount.id).count()
    return render(request, 'home.html', {'blogpost': blogs})

# @login_required
def detailView(request, slug):
    blogs = get_object_or_404(Post, url = slug)
    comments = Comment.objects.filter(title = blogs.id)
    comment_counter = Comment.objects.filter(title = blogs.id).count()
    modCount = Post.objects.get(id = blogs.id)
    if request.method == 'POST':
        comtext = request.POST.get('comments_area')
        newField = Comment(title = blogs, comment_text = comtext)
        newField.save()

        # form = PostComment(request.POST)
        # if form.is_valid():
            # Comment.objects.create(title = blogs) #New
            # form.save()
            
        modCount.commentcounter += 1
        modCount.save()

        return redirect(request.path_info)
    # else:
        # form = PostComment()
    return render(request, 'viewpost.html', {'post': blogs, 'comment': comments, 'ccounter': comment_counter}) #'view_form':form

# def commentView(request):
#     if request.method == 'POST':
#         form = PostComment(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(request.path_info)
#     else:
#         form = PostComment()

#     return render(request, 'viewpost.html', {'view_form': form})