from django.db import models
from participant.models import Participant

# Create your models here.
class Room(models.Model):
    created_by = models.ForeignKey(Participant, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    date_created = models.DateTimeField(auto_created=True)
    participants = models.ManyToManyField(Participant, related_name="participant")

    def __str__(self):
        return self.name


class Post(models.Model):
    created_by = models.ForeignKey(Participant, models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_created=True)
    title = models.CharField(max_length=500)
    post = models.TextField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return self.title