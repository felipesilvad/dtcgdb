# Generated by Django 3.1.2 on 2021-07-20 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0064_remove_effect_effect_keyword_int_2'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='evolution_cost_1_lv',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='card',
            name='evolution_cost_2_lv',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]