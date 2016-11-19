from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from datetime import timedelta
from .models import Post

# Create your views here.

def post_list(request):
    time = timezone.now() + timedelta(days = -24)
    select = Post.objects.filter(published_date__lte=timezone.now())
    posts = select.order_by('?')
    return render(request, 'blog/post_list.html', {'posts': posts, 'date': time})
        # request = everything from user via internet
        # 'blog/post_list.html' = temlate file
        # {} = objects for template to use

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
