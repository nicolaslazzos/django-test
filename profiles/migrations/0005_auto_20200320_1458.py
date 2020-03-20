# Generated by Django 2.1.5 on 2020-03-20 17:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_profile_profilepicture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='provinceId',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='provinces.Province'),
        ),
    ]