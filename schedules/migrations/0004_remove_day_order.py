# Generated by Django 2.1.5 on 2020-05-19 21:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0003_schedulesetting'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='day',
            name='order',
        ),
    ]
