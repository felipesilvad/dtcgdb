# Generated by Django 3.1.2 on 2021-01-21 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0051_auto_20210121_1159'),
    ]

    operations = [
        migrations.RenameField(
            model_name='effectkeyword',
            old_name='effect_keyword_desc',
            new_name='desc',
        ),
        migrations.RenameField(
            model_name='effectkeyword',
            old_name='effect_keyword_title',
            new_name='title',
        ),
    ]
