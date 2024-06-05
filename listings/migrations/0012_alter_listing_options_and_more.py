# Generated by Django 4.2.7 on 2024-05-16 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0011_auto_20240430_1235'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='listing',
            options={'ordering': ['-created_on']},
        ),
        migrations.RenameField(
            model_name='listing',
            old_name='created_at',
            new_name='created_on',
        ),
        migrations.RenameField(
            model_name='listing',
            old_name='updated_at',
            new_name='updated_on',
        ),
        migrations.AddField(
            model_name='listing',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]