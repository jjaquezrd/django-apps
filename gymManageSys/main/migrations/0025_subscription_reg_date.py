# Generated by Django 4.2.2 on 2023-06-11 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_subplan_validity_days'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='reg_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
