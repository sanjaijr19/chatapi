from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)



class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    message = models.CharField(max_length=1200)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message

    class Meta:
        ordering = ('timestamp',)

class GroupChat(models.Model):
    group_members = models.ForeignKey(User, on_delete=models.CASCADE,related_name='group')
    join_date = models.DateTimeField(auto_now_add=True)

    def Join(self):
        self.join_date = timezone.now()
        self.save()



