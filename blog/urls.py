from django.urls import path
from . import views

urlpatterns = [
    path('', views.display, name='display'),
    path('signup/', views.SignUp.as_view(), name = 'signup'),
    path('post/', views.post, name = "blog"),
    path('post/', views.post, name = "add_post"),
    path('<slug:slug>', views.detailView, name = "detail_view"),
    # path('post/comments', views.commentView, name= "view_comments"),

]