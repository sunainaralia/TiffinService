# Generated by Django 5.0.7 on 2024-07-16 01:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kitchen', '0010_order_payment_subscription_schedule'),
    ]

    operations = [
        migrations.RenameField(
            model_name='weeklyplan',
            old_name='breakfast',
            new_name='plans',
        ),
        migrations.RemoveField(
            model_name='weeklyplan',
            name='day',
        ),
        migrations.RemoveField(
            model_name='weeklyplan',
            name='dinner',
        ),
        migrations.RemoveField(
            model_name='weeklyplan',
            name='lunch',
        ),
    ]
