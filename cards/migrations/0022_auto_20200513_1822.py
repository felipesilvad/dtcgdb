# Generated by Django 3.0.4 on 2020-05-13 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0021_auto_20200513_0413'),
    ]

    operations = [
        migrations.AddField(
            model_name='set',
            name='price_1',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='set',
            name='price_2',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]