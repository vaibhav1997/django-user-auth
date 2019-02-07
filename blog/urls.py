from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.display, name='display'),
    path('signup/', views.SignUp.as_view(), name = 'signup'),
    path('post/', views.post, name = "blog"),
    path('post/', views.post, name = "add_post"),
    path('post/<int:post_id>', views.editpost, name = "edit_post"),
    path('<slug:slug>', views.detailView, name = "detail_view"),
    # path('post/comments', views.commentView, name= "view_comments"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)