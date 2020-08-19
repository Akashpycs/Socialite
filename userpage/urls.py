from django.contrib import admin
from django.urls import path, include
from . import views
from .views import Search_User, EditProfile

app_name = 'userpage'

urlpatterns = [
    path('', views.userHome, name='userHome'),
    path('post', views.post, name='post'),
    path('like_dislike', views.likePost, name='like_dislike_post'),
    path("delete/<int:ID>", views.delPost, name='delpost'),
    path("<str:username>", views.userProfile, name='user_profile'),
    path("slug/comment", views.comment, name='comment'),
    path("user/follow/<str:username>", views.follow, name="follow"),
    path("search/", Search_User.as_view(), name="search_user"),
    path("<str:username>/edit", EditProfile.as_view(), name="editprofile"),

]
