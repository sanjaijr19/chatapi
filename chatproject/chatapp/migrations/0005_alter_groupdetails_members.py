# Generated by Django 4.1.2 on 2022-11-15 04:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chatapp', '0004_alter_message_receiver'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupdetails',
            name='members',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='members', to=settings.AUTH_USER_MODEL),
        ),
    ]