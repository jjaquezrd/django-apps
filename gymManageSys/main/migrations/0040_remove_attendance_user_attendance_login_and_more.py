# Generated by Django 4.2.2 on 2023-06-14 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0039_remove_attendance_hora_entrada'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance',
            name='user',
        ),
        migrations.AddField(
            model_name='attendance',
            name='Login',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='attendance',
            name='Logout',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='attendance',
            name='SelectWorkout',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='attendance',
            name='phonenumber',
            field=models.CharField(max_length=15, null=True),
        ),
    ]