# Generated by Django 5.0.7 on 2024-07-14 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0005_operatinghours'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraddress',
            name='latitude',
            field=models.DecimalField(decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='useraddress',
            name='longitude',
            field=models.DecimalField(decimal_places=6, max_digits=9, null=True),
        ),
    ]
