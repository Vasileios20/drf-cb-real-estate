# Generated by Django 4.2.7 on 2024-05-30 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0017_listing_county_alter_listing_sub_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='currency',
            field=models.CharField(default='€', max_length=255),
        ),
    ]
