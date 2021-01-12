from django.urls import path, include
from comment import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path("addcomment/to_post/", views.post_comment, name="add_post_comment"),
]

app_name = "comment"
