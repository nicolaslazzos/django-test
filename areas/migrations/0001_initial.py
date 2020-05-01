# Generated by Django 2.1.5 on 2020-03-26 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('softDelete', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
