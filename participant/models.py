from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Participant(AbstractUser):
    profile_pic = models.ImageField(upload_to='images/', null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.username