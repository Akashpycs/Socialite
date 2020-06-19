from django.contrib import admin
from .models import Post, Profile, Like, Following
admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Profile)
admin.site.register(Following)
