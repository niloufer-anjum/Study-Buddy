from django.db import models
from participant.models import Participant
from topic.models import Topic

# Create your models here.
class Room(models.Model):
    created_by = models.ForeignKey(Participant, on_delete=models.CASCADE, related_name="room_creator")
    name = models.CharField(max_length=100, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    participants = models.ManyToManyField(Participant, related_name="participant")
    topic = models.ManyToManyField(Topic, related_name="tags", blank=True)

    def __str__(self):
        return self.name
