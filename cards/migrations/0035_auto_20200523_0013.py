# Generated by Django 3.0.4 on 2020-05-23 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0034_auto_20200522_2350'),
    ]

    operations = [
        migrations.AddField(
            model_name='new',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.RemoveField(
            model_name='new',
            name='releated_cards',
        ),
        migrations.AddField(
            model_name='new',
            name='releated_cards',
            field=models.ManyToManyField(blank=True, null=True, to='cards.Card'),
        ),
    ]
