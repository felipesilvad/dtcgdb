# Generated by Django 3.0.4 on 2020-05-09 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0003_card_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='image_en',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='card',
            name='image_jp',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]