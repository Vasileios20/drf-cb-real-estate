# Generated by Django 3.2.4 on 2024-04-11 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0007_auto_20240218_1655'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='latitude',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='listing',
            name='longitude',
            field=models.FloatField(default=0.0),
        ),
    ]
