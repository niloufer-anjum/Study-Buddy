from django.shortcuts import render
from . models import Topic
from participant.models import Participant
from room.models import Room

from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(
    login_url='/auth/login'
)
def topics(request):
    topics = Topic.objects.all()
    context = {
        "topics": topics
    }
    if request.method == 'POST':
        create_topic(request)
    return render(request, "topics.html", context)


@login_required(
    login_url='/auth/login'
)
def create_topic(request):
        d = {
            "topic_name":request.POST["topic_name"],
            "created_by": Participant.objects.get(username=request.user.username)
        }
        
        topic = Topic.objects.create(**d)
        return render(request, "topics.html", {"topic": topic})