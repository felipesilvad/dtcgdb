# Generated by Django 3.1.2 on 2020-12-24 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0042_card_amazon_jp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='releated_cards',
            field=models.ManyToManyField(blank=True, to='cards.Card'),
        ),
    ]
