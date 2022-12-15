from django.shortcuts import render
from .models import Room, Post

# Create your views here.
def index(request):
    print(request.user)
    rooms_list = Room.objects.filter(participants=request.user.id)
    context = {"rooms": rooms_list}
    return render(request, "rooms.html", context)

def room(request, slug):
    rooms_list = Room.objects.filter(participants=request.user.id)
    room = Room.objects.filter(name=slug)
    posts = Post.objects.filter(room=room[0].id)
    print(posts)
    context = {
        "rooms_list": rooms_list,
        "room_name": room[0].name,
        "room_creator": room[0].created_by,
        "room_creation_date": room[0].date_created,
        "participants": room[0].participants,
        "posts": posts
    }
    return render(request, "room.html", context)