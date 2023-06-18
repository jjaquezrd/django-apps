# Generated by Django 4.2.2 on 2023-06-09 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_rename_mobil_subscriber_mobile_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('is_active', models.BooleanField(default=False)),
                ('detail', models.TextField()),
                ('img', models.ImageField(null=True, upload_to='trainers/')),
            ],
        ),
        migrations.AlterField(
            model_name='subscriber',
            name='img',
            field=models.ImageField(null=True, upload_to='subs/'),
        ),
    ]