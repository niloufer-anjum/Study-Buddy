from django.db import models
from participant.models import Participant

# Create your models here.
class Topic(models.Model):
    topic_name = models.CharField(max_length=500, unique=True)
    created_time = models.DateTimeField(auto_created=True)
    created_by = models.ForeignKey(Participant, models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.topic_name
