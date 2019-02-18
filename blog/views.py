from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.urls import reverse_lazy
from django.views import generic
from .models import Post, Comment
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required  #Use only when page view (True) for login
from .forms import CustomUserCreationForm, AddPost, EditPost 
from django.db.models import Q
from django.core import serializers
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
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

    paginator = Paginator(blogs, 3)
    page = request.GET.get('page')
    disp = paginator.get_page(page)
    # disp = paginate.page(1)
    # if request.is_ajax():
    #     pageNo = request.GET.get("page")
    #     disp = paginate.page(pageNo)
    #     # ranges = {"page-range":paginate.page_range}
    #     data = serializers.serialize('json', disp)
    #     return HttpResponse(data)

    return render(request, 'home.html', {'blogpost': disp})
    

# @login_required
def detailView(request, slug):
    blogs = get_object_or_404(Post, url = slug)
    comments = Comment.objects.filter(title = blogs.id)
    comment_counter = Comment.objects.filter(title = blogs.id).count()
    modCount = Post.objects.get(id = blogs.id)
    
   
    # if request.method == 'POST':
    if request.is_ajax():
        # message = "hello"
        # Now----
        comtext = request.GET.get('comments_area')

        newField = Comment(title = blogs, comment_text = comtext)
        newField.save()
        # Now -----------

        # form = PostComment(request.POST)
        # if form.is_valid():
            # Comment.objects.create(title = blogs) #New
            # form.save()
        # # Now -------
        modCount.commentcounter += 1
        modCount.save()
        data = {"count":modCount.commentcounter, "text":newField.comment_text, "created_date":newField.created_at}
        return JsonResponse(data)

        # return redirect(request.path_info) #Uncomment?
        # Now-----------------
    else:
        return render(request, 'viewpost.html', {'post': blogs, 'comment': comments, 'ccounter': comment_counter}) #'view_form':form
    #     # form = PostComment()
    

def vCom(request):
    if request.is_ajax():
        return render(request, 'comments.html')

def searchQuery(request):
    if request.is_ajax():
        searchText = request.POST.get("search_area")
        results = Post.objects.filter(Q(title__icontains=searchText) | Q(content__icontains=searchText) | Q(author__icontains=searchText))
        data = serializers.serialize('json', results)
        return HttpResponse(data)

