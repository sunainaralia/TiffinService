# Generated by Django 5.0.7 on 2024-07-16 10:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kitchen', '0018_remove_subscription_discount_and_more'),
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='payment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subscription', to='payment.payment'),
        ),
    ]
