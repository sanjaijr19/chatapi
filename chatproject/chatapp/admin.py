from django.contrib import admin
from .models import UserProfile,Message,GroupChat
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Message)
admin.site.register(GroupChat)
