# Generated by Django 5.0.7 on 2024-07-19 04:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kitchen', '0027_cancelorder_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subscription',
            old_name='brekfast',
            new_name='breakfast',
        ),
    ]
