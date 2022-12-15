from django.shortcuts import render
from . models import Topic

# Create your views here.
def topic(request):
    topics = Topic.objects.all()
    context = {
        "topics": topics
    }
    print(context)

    return render(request, "topics.html", context)