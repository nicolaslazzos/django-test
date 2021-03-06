# Generated by Django 2.1.5 on 2020-05-04 18:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('commerces', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Court',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.FloatField()),
                ('lightPrice', models.FloatField(blank=True, null=True)),
                ('lightHour', models.CharField(blank=True, max_length=5, null=True)),
                ('disabledFrom', models.DateTimeField(blank=True, null=True)),
                ('disabledTo', models.DateTimeField(blank=True, null=True)),
                ('softDelete', models.DateTimeField(blank=True, null=True)),
                ('commerceId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commerces.Commerce')),
            ],
        ),
        migrations.CreateModel(
            name='CourtType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.URLField(blank=True, max_length=300, null=True)),
                ('softDelete', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='GroundType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('softDelete', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='court',
            name='courtTypeId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courts.CourtType'),
        ),
        migrations.AddField(
            model_name='court',
            name='groundTypeId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courts.GroundType'),
        ),
    ]
