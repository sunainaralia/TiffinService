# Generated by Django 5.0.7 on 2024-07-16 05:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kitchen', '0014_remove_todaymeal_time_of_day'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todaymeal',
            old_name='menu',
            new_name='plans',
        ),
    ]
