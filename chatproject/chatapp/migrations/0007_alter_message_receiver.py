# Generated by Django 4.1.2 on 2022-11-15 06:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0006_alter_message_receiver'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='receiver',
            field=models.ForeignKey(db_constraint=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to='chatapp.groupdetails'),
        ),
    ]
