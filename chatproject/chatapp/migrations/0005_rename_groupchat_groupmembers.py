# Generated by Django 4.1.2 on 2022-11-07 09:43

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chatapp', '0004_alter_message_receiver'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='GroupChat',
            new_name='GroupMembers',
        ),
    ]
