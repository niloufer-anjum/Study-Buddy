from django.http import HttpResponse
from django.shortcuts import render, redirect
from post.models import Post, Comment
from room.models import Room, Participant
from topic.models import Topic
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(
    login_url='/auth/login'
)
def index(request):
    if request.user.is_authenticated:
        participant = Participant.objects.get(username=request.user.username)
        rooms_list = Room.objects.filter(participants=participant)
        recent_posts = Post.objects.filter(room__participants=participant).order_by('created_at')[:15]
        comments = Comment.objects.filter(post__room__participants=participant).order_by('created_at')[:5]
        topics_list = Topic.objects.all().order_by('created_time')[:5]
        context = {
            "rooms": rooms_list,
            "topics": topics_list,
            "recent_posts": recent_posts,
            "comments": comments
        }
        return render(request, "index.html", context)
    return redirect("login")