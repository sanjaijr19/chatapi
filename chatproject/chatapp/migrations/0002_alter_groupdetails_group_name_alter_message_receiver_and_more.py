# Generated by Django 4.1.2 on 2022-11-09 08:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chatapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupdetails',
            name='group_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group_name', to='chatapp.groupname'),
        ),
        migrations.AlterField(
            model_name='message',
            name='receiver',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to='chatapp.groupname'),
        ),
        migrations.AlterField(
            model_name='message',
            name='sender',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, related_name='sender', to=settings.AUTH_USER_MODEL),
        ),
    ]