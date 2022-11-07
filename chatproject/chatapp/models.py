from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class GroupMembers(models.Model):
    group_members = models.OneToOneField(User,on_delete=models.CASCADE, related_name='group', unique=True)
    join_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.group_members)

    # def __str__(self):
    #     return str(self.join_date)
    # def __str__(self):
    #     return "%s %s" % (self.group_members, self.join_date)

    def Join(self):
        self.join_date = timezone.now()
        self.save()


class Group_Name(models.Model):
    group_name = models.CharField(max_length=25)
    name = models.ManyToManyField(GroupMembers)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.group_name
    def Time(self):
        self.date = timezone.now()
        self.save()

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender',db_constraint=False)
    receiver = models.ForeignKey(Group_Name, on_delete=models.CASCADE,related_name='receiver',db_constraint=False)
    message = models.CharField(max_length=1200)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s %s" % (self.sender, self.receiver)
    class Meta:
        ordering = ('timestamp',)


