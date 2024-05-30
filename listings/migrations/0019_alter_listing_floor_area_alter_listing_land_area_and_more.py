# Generated by Django 4.2.7 on 2024-05-30 09:27

from django.db import migrations, models
import listings.models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0018_listing_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='floor_area',
            field=models.FloatField(validators=[listings.models.validate_zero]),
        ),
        migrations.AlterField(
            model_name='listing',
            name='land_area',
            field=models.FloatField(default=0, validators=[listings.models.validate_zero]),
        ),
        migrations.AlterField(
            model_name='listing',
            name='price',
            field=models.FloatField(validators=[listings.models.validate_zero]),
        ),
    ]
