# Generated by Django 5.0.7 on 2024-07-16 01:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kitchen', '0009_remove_weeklyplan_plans_extrameal_user_and_more'),
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_payment', to='payment.payment'),
        ),
        migrations.AddField(
            model_name='subscription',
            name='schedule',
            field=models.ManyToManyField(related_name='scheduled_subscription', to='kitchen.scheduleorder'),
        ),
    ]
