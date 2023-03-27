from django.db import models
from participant.models import Participant
from room.models import Room

# Create your models here.
class Post(models.Model):
    created_by = models.ForeignKey(Participant, models.SET_NULL, blank=True, null=True, related_name="post_creator")
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=500)
    post = models.TextField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Like(models.Model):
    liked_by = models.ForeignKey(Participant, models.SET_NULL, blank=True, null=True, related_name="post_like")
    liked_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    

class Comment(models.Model):
    created_by = models.ForeignKey(Participant, models.SET_NULL, blank=True, null=True, related_name="comment_creator")
    created_at = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(max_length=500)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    like = models.ForeignKey(Like, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return self.comment
