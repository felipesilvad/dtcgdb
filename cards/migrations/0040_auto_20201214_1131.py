# Generated by Django 3.1.2 on 2020-12-14 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0039_auto_20200620_1922'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='yuyu_tei',
            field=models.URLField(blank=True, max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='effect_keyword_1',
            field=models.CharField(blank=True, choices=[('Pierce', 'Pierce'), ('Blocker', 'Blocker'), ('Jamming', 'Jamming'), ('Draw', 'Draw'), ('Recovery (Deck) +', 'Recovery (Deck) +'), ('Security Attack +', 'Security Attack +'), ('Security Attack -', 'Security Attack -'), ('Vengeance', 'Vengeance'), ('Download', 'Download'), ('De-Digivolve', 'De-Digivolve')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='effect_keyword_2',
            field=models.CharField(blank=True, choices=[('Pierce', 'Pierce'), ('Blocker', 'Blocker'), ('Jamming', 'Jamming'), ('Draw', 'Draw'), ('Recovery (Deck) +', 'Recovery (Deck) +'), ('Security Attack +', 'Security Attack +'), ('Security Attack -', 'Security Attack -'), ('Vengeance', 'Vengeance'), ('Download', 'Download'), ('De-Digivolve', 'De-Digivolve')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='effect_keyword_3',
            field=models.CharField(blank=True, choices=[('Pierce', 'Pierce'), ('Blocker', 'Blocker'), ('Jamming', 'Jamming'), ('Draw', 'Draw'), ('Recovery (Deck) +', 'Recovery (Deck) +'), ('Security Attack +', 'Security Attack +'), ('Security Attack -', 'Security Attack -'), ('Vengeance', 'Vengeance'), ('Download', 'Download'), ('De-Digivolve', 'De-Digivolve')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='evolutionary_effect_keyword_1',
            field=models.CharField(blank=True, choices=[('Pierce', 'Pierce'), ('Blocker', 'Blocker'), ('Jamming', 'Jamming'), ('Draw', 'Draw'), ('Recovery (Deck) +', 'Recovery (Deck) +'), ('Security Attack +', 'Security Attack +'), ('Security Attack -', 'Security Attack -'), ('Vengeance', 'Vengeance'), ('Download', 'Download'), ('De-Digivolve', 'De-Digivolve')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='evolutionary_effect_keyword_2',
            field=models.CharField(blank=True, choices=[('Pierce', 'Pierce'), ('Blocker', 'Blocker'), ('Jamming', 'Jamming'), ('Draw', 'Draw'), ('Recovery (Deck) +', 'Recovery (Deck) +'), ('Security Attack +', 'Security Attack +'), ('Security Attack -', 'Security Attack -'), ('Vengeance', 'Vengeance'), ('Download', 'Download'), ('De-Digivolve', 'De-Digivolve')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='evolutionary_effect_keyword_3',
            field=models.CharField(blank=True, choices=[('Pierce', 'Pierce'), ('Blocker', 'Blocker'), ('Jamming', 'Jamming'), ('Draw', 'Draw'), ('Recovery (Deck) +', 'Recovery (Deck) +'), ('Security Attack +', 'Security Attack +'), ('Security Attack -', 'Security Attack -'), ('Vengeance', 'Vengeance'), ('Download', 'Download'), ('De-Digivolve', 'De-Digivolve')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='new',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]