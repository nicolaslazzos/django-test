# Generated by Django 2.1.5 on 2020-05-12 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day',
            name='id',
            field=models.SmallIntegerField(primary_key=True, serialize=False, unique=True),
        ),
    ]
