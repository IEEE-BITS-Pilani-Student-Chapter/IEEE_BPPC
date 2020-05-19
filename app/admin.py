from django.contrib import admin

from .models import Post, Developer

admin.site.register(Post)
admin.site.register(Developer)