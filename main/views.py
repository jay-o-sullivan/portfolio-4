from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Category, Comment
from django.contrib.auth.decorators import login_required


def home(request):
    posts = Post.objects.all().order_by('-created_at')
    categories = Category.objects.all()
    return render(request, 'main/home.html', {'posts': posts, 'categories': categories})


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'main/post_detail.html', {'post': post})


@login_required
def upvote_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.upvotes += 1
    post.save()
    return redirect('home')


@login_required
def downvote_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.downvotes += 1
    post.save()
    return redirect('home')


@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        content = request.POST.get('content')
        Comment.objects.create(content=content, author=request.user, post=post)
    return redirect('post_detail', post_id=post_id)
