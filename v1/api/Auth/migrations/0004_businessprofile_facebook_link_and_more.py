# Generated by Django 5.0.7 on 2024-07-11 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0003_businessprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='businessprofile',
            name='facebook_link',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='businessprofile',
            name='instagram_link',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='businessprofile',
            name='twitter_link',
            field=models.URLField(blank=True),
        ),
    ]
