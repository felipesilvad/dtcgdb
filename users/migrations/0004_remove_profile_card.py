# Generated by Django 3.1.2 on 2020-12-24 19:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_card'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='card',
        ),
    ]
