# Generated by Django 2.1.5 on 2020-05-01 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='visible',
            field=models.BooleanField(default=True),
        ),
    ]
