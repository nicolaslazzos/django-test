# Generated by Django 2.1.5 on 2020-05-12 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='clientName',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='clientPhone',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
