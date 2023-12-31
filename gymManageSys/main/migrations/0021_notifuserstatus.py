# Generated by Django 4.2.2 on 2023-06-11 00:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0020_alter_notify_read_by_trainer_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='NotifUserStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False)),
                ('notif', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.notify')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
