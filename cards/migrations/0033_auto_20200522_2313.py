# Generated by Django 3.0.4 on 2020-05-23 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0032_newc_card_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='card',
            name='new_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='card',
            name='new_parallel',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='NewC',
        ),
    ]
