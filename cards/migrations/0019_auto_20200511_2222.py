# Generated by Django 3.0.4 on 2020-05-12 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0018_auto_20200511_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='effect_keyword_1',
            field=models.CharField(blank=True, choices=[('Pierce', 'Pierce'), ('Blocker', 'Blocker'), ('Jamming', 'Jamming'), ('Draw', 'Draw'), ('When Placed', 'When Placed'), ('Recovery (Deck) +', 'Recovery (Deck) +'), ('Security Attack +', 'Security Attack +'), ('Security Attack -', 'Security Attack -')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='effect_keyword_2',
            field=models.CharField(blank=True, choices=[('Pierce', 'Pierce'), ('Blocker', 'Blocker'), ('Jamming', 'Jamming'), ('Draw', 'Draw'), ('When Placed', 'When Placed'), ('Recovery (Deck) +', 'Recovery (Deck) +'), ('Security Attack +', 'Security Attack +'), ('Security Attack -', 'Security Attack -')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='effect_keyword_3',
            field=models.CharField(blank=True, choices=[('Pierce', 'Pierce'), ('Blocker', 'Blocker'), ('Jamming', 'Jamming'), ('Draw', 'Draw'), ('When Placed', 'When Placed'), ('Recovery (Deck) +', 'Recovery (Deck) +'), ('Security Attack +', 'Security Attack +'), ('Security Attack -', 'Security Attack -')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='evolutionary_effect_keyword_1',
            field=models.CharField(blank=True, choices=[('Pierce', 'Pierce'), ('Blocker', 'Blocker'), ('Jamming', 'Jamming'), ('Draw', 'Draw'), ('When Placed', 'When Placed'), ('Recovery (Deck) +', 'Recovery (Deck) +'), ('Security Attack +', 'Security Attack +'), ('Security Attack -', 'Security Attack -')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='evolutionary_effect_keyword_2',
            field=models.CharField(blank=True, choices=[('Pierce', 'Pierce'), ('Blocker', 'Blocker'), ('Jamming', 'Jamming'), ('Draw', 'Draw'), ('When Placed', 'When Placed'), ('Recovery (Deck) +', 'Recovery (Deck) +'), ('Security Attack +', 'Security Attack +'), ('Security Attack -', 'Security Attack -')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='evolutionary_effect_keyword_3',
            field=models.CharField(blank=True, choices=[('Pierce', 'Pierce'), ('Blocker', 'Blocker'), ('Jamming', 'Jamming'), ('Draw', 'Draw'), ('When Placed', 'When Placed'), ('Recovery (Deck) +', 'Recovery (Deck) +'), ('Security Attack +', 'Security Attack +'), ('Security Attack -', 'Security Attack -')], max_length=100, null=True),
        ),
    ]