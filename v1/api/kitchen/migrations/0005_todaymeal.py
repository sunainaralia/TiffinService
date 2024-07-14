# Generated by Django 5.0.7 on 2024-07-13 15:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0005_operatinghours'),
        ('kitchen', '0004_alter_dayplan_breakfast_alter_dayplan_day_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TodayMeal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_of_day', models.CharField(max_length=100)),
                ('kitchen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='today_meal', to='Auth.businessprofile')),
                ('menu', models.ManyToManyField(related_name='today_meal', to='kitchen.menuitem')),
            ],
        ),
    ]
