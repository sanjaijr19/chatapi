from django.contrib import admin
from .models import Message,GroupDetails,GroupName
# Register your models here.

admin.site.register(Message)
# admin.site.register(GroupMembers)
admin.site.register(GroupName)
admin.site.register(GroupDetails)

