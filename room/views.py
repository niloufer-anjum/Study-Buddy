from django.shortcuts import render
from django.db.models import Q
from .models import Room
from post.models import Post
from participant.models import Participant
import datetime

from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(
    login_url='/auth/login'
)
def index(request):
    print(request.GET.get('q'))
    if request.GET.get('q'):
        q = request.GET.get('q')
        rooms_list = Room.objects.filter(
            Q(topic__topic_name__icontains=q) |
            Q(name__icontains=q) 
        )
    else:
        participant = Participant.objects.get(username=request.user.username)
        rooms_list = Room.objects.filter(participants=participant)[:5]

    if request.method == 'POST':
        return room(request, create_room(request))
    return render(request, "rooms.html", {"rooms": rooms_list})

@login_required(
    login_url='/auth/login'
)
def room(request, room):
    participant = Participant.objects.get(username=request.user.username)
    rooms_list = Room.objects.filter(participants=participant)[:5]
    room = Room.objects.filter(name=room)
    posts = Post.objects.filter(room=room[0].id)
    context = {
        "rooms_list": rooms_list,
        "room_name": room[0].name,
        "room_creator": room[0].created_by,
        "room_creation_date": room[0].date_created,
        "participants": room[0].participants,
        "posts": posts
    }
    return render(request, "room.html", context)

@login_required(
    login_url='/auth/login'
)
def create_room(request):
    if request.method == 'POST':
        participant = Participant.objects.get(username=request.user.username)
        d = {
            "created_by": participant,
            "name": request.POST["room_name"],
            "date_created": datetime.datetime.now(),
        }
        room = Room.objects.create(**d)
        room.participants.add(request.user.id)
    return room.name