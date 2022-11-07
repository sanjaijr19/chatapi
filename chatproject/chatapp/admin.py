from django.contrib import admin
from .models import Message,GroupMembers,Group_Name
# Register your models here.

admin.site.register(Message)
admin.site.register(GroupMembers)
admin.site.register(Group_Name)

