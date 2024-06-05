# Generated by Django 4.2.7 on 2024-05-29 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0015_rename_elevator_amenities_auction_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='municipality',
            field=models.CharField(default=' ', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listing',
            name='sub_type',
            field=models.CharField(choices=[('apartment', 'Apartment'), ('maisonette', 'Maisonette'), ('detached', 'Detached'), ('semi_detached', 'Semi Detached'), ('terraced', 'Terraced'), ('bungalow', 'Bungalow'), ('villa', 'Villa'), ('farmhouse', 'Farmhouse'), ('building', 'Building'), ('shop', 'Shop'), ('office', 'Office'), ('warehouse', 'Warehouse'), ('hotel', 'Hotel'), ('industrial', 'Industrial'), ('agricultural', 'Agricultural'), ('other', 'Other')], default='apartment', max_length=255),
        ),
        migrations.AlterField(
            model_name='listing',
            name='type',
            field=models.CharField(choices=[('residential', 'Residential'), ('land', 'Land'), ('commercial', 'Commercial')], default='residential', max_length=255),
        ),
    ]