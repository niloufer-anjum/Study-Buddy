from django.contrib.auth.forms import UserCreationForm

from .models import Participant

class ParticipantCreationForm(UserCreationForm):
    class Meta:
        model = Participant
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2']