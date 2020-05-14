# Generated by Django 2.1.5 on 2020-05-14 19:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('commerces', '0003_auto_20200514_1931'),
        ('profiles', '0003_auto_20200514_1931'),
        ('employees', '0002_auto_20200504_1854'),
        ('reservations', '0003_auto_20200513_2140'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField(blank=True, null=True)),
                ('read', models.BooleanField(default=False)),
                ('date', models.DateTimeField()),
                ('acceptanceDate', models.DateTimeField(blank=True, null=True)),
                ('rejectionDate', models.DateTimeField(blank=True, null=True)),
                ('softDelete', models.DateTimeField(blank=True, null=True)),
                ('commerceId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='commerces.Commerce')),
                ('employeeId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='employees.Employee')),
                ('profileId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='profiles.Profile')),
                ('reservationId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='reservations.Reservation')),
            ],
        ),
        migrations.CreateModel(
            name='NotificationToken',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('profileId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='NotificationType',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('softDelete', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
