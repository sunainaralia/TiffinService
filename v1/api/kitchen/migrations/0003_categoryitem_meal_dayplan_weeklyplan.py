# Generated by Django 5.0.7 on 2024-07-13 00:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0005_operatinghours'),
        ('kitchen', '0002_rename_kitchen_menuitem_kitchen_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meal_type', models.CharField(max_length=20)),
                ('items', models.ManyToManyField(to='kitchen.categoryitem')),
            ],
        ),
        migrations.CreateModel(
            name='DayPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=20)),
                ('breakfast', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='breakfast', to='kitchen.meal')),
                ('dinner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='dinner', to='kitchen.meal')),
                ('lunch', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='lunch', to='kitchen.meal')),
            ],
        ),
        migrations.CreateModel(
            name='WeeklyPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kitchen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='weekly_plans', to='Auth.businessprofile')),
                ('plans', models.ManyToManyField(to='kitchen.dayplan')),
            ],
        ),
    ]
