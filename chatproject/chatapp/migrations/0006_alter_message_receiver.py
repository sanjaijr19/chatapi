# Generated by Django 4.1.2 on 2022-11-15 05:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0005_alter_groupdetails_members'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='receiver',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to='chatapp.groupdetails'),
        ),
    ]
