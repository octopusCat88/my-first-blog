from django.contrib import admin
from .models import Post # import the Post model

admin.site.register(Post) # make model visible on admin page
