# Generated by Django 3.0.4 on 2020-05-10 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0011_auto_20200510_0218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='effect_blue_1',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='effect_blue_2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='effect_blue_3',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='effect_purple_1',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='effect_purple_2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='effect_purple_3',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
