# Generated by Django 3.0.4 on 2020-05-15 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0024_auto_20200514_2341'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='image_parallel',
            field=models.ImageField(blank=True, upload_to='parallel/'),
        ),
    ]
