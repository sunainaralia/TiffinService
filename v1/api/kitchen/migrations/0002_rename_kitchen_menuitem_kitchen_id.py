# Generated by Django 5.0.7 on 2024-07-12 14:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kitchen', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menuitem',
            old_name='kitchen',
            new_name='kitchen_id',
        ),
    ]
