# Generated by Django 3.0.4 on 2020-05-10 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0013_auto_20200510_0301'),
    ]

    operations = [
        migrations.RenameField(
            model_name='card',
            old_name='evolutionary_effect',
            new_name='evolutionary_effect_txt_1',
        ),
        migrations.AddField(
            model_name='card',
            name='evolutionary_effect_blue_1',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='card',
            name='evolutionary_effect_blue_2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='card',
            name='evolutionary_effect_blue_3',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='card',
            name='evolutionary_effect_keyword_1',
            field=models.CharField(blank=True, choices=[('Pierce', 'Pierce'), ('Blocker', 'Blocker'), ('Jamming', 'Jamming'), ('Draw 1', 'Draw 1'), ('Draw 2', 'Draw 2'), ('When Placed', 'When Placed'), ('Recovery +1 (Deck)', 'Recovery +1 (Deck)'), ('Security Attack +1', 'Security Attack +1'), ('Security Attack + 2', 'Security Attack + 2'), ('Security Attack - 3', 'Security Attack - 3')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='card',
            name='evolutionary_effect_keyword_2',
            field=models.CharField(blank=True, choices=[('Pierce', 'Pierce'), ('Blocker', 'Blocker'), ('Jamming', 'Jamming'), ('Draw 1', 'Draw 1'), ('Draw 2', 'Draw 2'), ('When Placed', 'When Placed'), ('Recovery +1 (Deck)', 'Recovery +1 (Deck)'), ('Security Attack +1', 'Security Attack +1'), ('Security Attack + 2', 'Security Attack + 2'), ('Security Attack - 3', 'Security Attack - 3')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='card',
            name='evolutionary_effect_keyword_3',
            field=models.CharField(blank=True, choices=[('Pierce', 'Pierce'), ('Blocker', 'Blocker'), ('Jamming', 'Jamming'), ('Draw 1', 'Draw 1'), ('Draw 2', 'Draw 2'), ('When Placed', 'When Placed'), ('Recovery +1 (Deck)', 'Recovery +1 (Deck)'), ('Security Attack +1', 'Security Attack +1'), ('Security Attack + 2', 'Security Attack + 2'), ('Security Attack - 3', 'Security Attack - 3')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='card',
            name='evolutionary_effect_purple_1',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='card',
            name='evolutionary_effect_purple_2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='card',
            name='evolutionary_effect_purple_3',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='card',
            name='evolutionary_effect_txt_2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='card',
            name='evolutionary_effect_txt_3',
            field=models.TextField(blank=True, null=True),
        ),
    ]