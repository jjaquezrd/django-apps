# Generated by Django 4.2.2 on 2023-06-11 06:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0022_assignsubscriber'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignsubscriber',
            name='subscriber',
        ),
        migrations.AddField(
            model_name='assignsubscriber',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='assignsubscriber',
            name='trainer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.trainer'),
        ),
    ]
