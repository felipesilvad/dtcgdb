# Generated by Django 3.1.2 on 2021-01-13 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0044_auto_20210113_2014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='digimon',
            name='image',
            field=models.ImageField(blank=True, upload_to='digimon-icons/'),
        ),
    ]
