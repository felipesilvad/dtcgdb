# Generated by Django 3.1.2 on 2021-01-13 22:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_profile_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='quantity',
        ),
    ]
