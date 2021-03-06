# Generated by Django 3.1.2 on 2020-12-26 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0043_auto_20201224_1358'),
        ('users', '0005_profile_card'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='bt1001',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='bt1002',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='bt1003',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='bt1004',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='card',
        ),
        migrations.AddField(
            model_name='profile',
            name='user_cards',
            field=models.ManyToManyField(to='cards.Card'),
        ),
    ]
