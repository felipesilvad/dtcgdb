# Generated by Django 3.1.2 on 2021-01-21 14:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0050_auto_20210121_1156'),
    ]

    operations = [
        migrations.CreateModel(
            name='EffectKeyword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('effect_keyword_title', models.CharField(blank=True, max_length=100, null=True)),
                ('effect_keyword_desc', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='effect',
            name='effect_keyword',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cards.effectkeyword'),
        ),
    ]
