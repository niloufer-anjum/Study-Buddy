from django.shortcuts import render, redirect
from participant.forms import ParticipantCreationForm
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login
from participant.models import Participant
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model


# Create your views here.
@login_required(
    login_url='/auth/login'
)
def settings(request):
    user = get_object_or_404(Participant, username=request.user)
    return render(request, "settings.html", {"user": user})

def signup(request):
    if request.POST:
        form = ParticipantCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            print("logged in!")
            return redirect('home')
    else:
        form = ParticipantCreationForm()
    return render(request, 'registration/signup.html', {'form': form})