# main/views.py

from django.shortcuts import render, get_object_or_404
from .models import Post, Category


def home(request):
    posts = Post.objects.all().order_by('-created_at')
    categories = Category.objects.all()
    return render(request, 'main/home.html', {'posts': posts, 'categories': categories})


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'main/post_detail.html', {'post': post})
