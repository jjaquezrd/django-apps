# Generated by Django 4.2.2 on 2023-06-14 06:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0041_remove_attendance_phonenumber_attendance_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='plan',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.subplan'),
        ),
    ]
