# Generated by Django 4.1.2 on 2022-11-15 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0011_alter_message_sender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='receiver',
            field=models.ForeignKey(db_constraint=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to='chatapp.groupdetails'),
        ),
    ]
