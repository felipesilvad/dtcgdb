# Generated by Django 3.1.2 on 2020-12-24 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bt1001',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='bt1002',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='bt1003',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='bt1004',
            field=models.IntegerField(null=True),
        ),
    ]
