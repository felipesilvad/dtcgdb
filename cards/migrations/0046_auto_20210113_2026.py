# Generated by Django 3.1.2 on 2021-01-13 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0045_auto_20210113_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='set',
            name='image',
            field=models.ImageField(blank=True, upload_to='sets/'),
        ),
        migrations.AlterField(
            model_name='set',
            name='produc_image_1',
            field=models.ImageField(blank=True, upload_to='sets/'),
        ),
        migrations.AlterField(
            model_name='set',
            name='produc_image_2',
            field=models.ImageField(blank=True, upload_to='sets/'),
        ),
    ]