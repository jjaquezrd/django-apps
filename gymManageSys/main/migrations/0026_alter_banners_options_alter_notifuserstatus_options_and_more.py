# Generated by Django 4.2.2 on 2023-06-11 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_subscription_reg_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='banners',
            options={'verbose_name_plural': 'Banners'},
        ),
        migrations.AlterModelOptions(
            name='notifuserstatus',
            options={'verbose_name_plural': 'Notification Status'},
        ),
        migrations.AddField(
            model_name='trainer',
            name='facebook',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='trainer',
            name='pinterest',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='trainer',
            name='twitter',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='trainer',
            name='youtube',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
