from django.contrib import admin

from Instagram.models import Post, InstaUser, Like
# Register your models here.

admin.site.register(Post)
admin.site.register(InstaUser)
admin.site.register(Like)