# Generated by Django 3.0 on 2020-03-18 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userpage', '0008_profile_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='post',
        ),
    ]
