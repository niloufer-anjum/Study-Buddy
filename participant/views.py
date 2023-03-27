from django.shortcuts import render, redirect
from participant.models import Participant
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(
    login_url='/auth/login'
)
def profile(request, user):
    if request.user.is_authenticated:
        participant = Participant.objects.filter(username=user)
        return render(request, "profile.html", {"user": participant[0]})
    return redirect('login')