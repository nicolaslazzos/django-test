# Generated by Django 2.1.5 on 2020-04-07 04:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('commerces', '0001_initial'),
        ('profiles', '0007_auto_20200326_0347'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clientId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.Profile')),
                ('commerceId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commerces.Commerce')),
            ],
        ),
    ]