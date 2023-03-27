from django.shortcuts import render
from .models import Post, Comment, Like

from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(
    login_url='/auth/login'
)
def index(request, post):
    post = Post.objects.get(title=post)
    comments = Comment.objects.filter(post=post)
    likes = Like.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "likes": likes.count,
    }
    return render(request, "post.html", context)