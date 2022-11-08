from django.contrib import admin
from .models import Message,GroupDetails
# Register your models here.

admin.site.register(Message)
# admin.site.register(GroupMembers)
admin.site.register(GroupDetails)

