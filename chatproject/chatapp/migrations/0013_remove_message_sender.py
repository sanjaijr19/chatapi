# Generated by Django 4.1.2 on 2022-11-16 03:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0012_alter_message_receiver'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='sender',
        ),
    ]
