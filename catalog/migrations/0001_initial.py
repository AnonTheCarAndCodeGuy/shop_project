# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('body_type', models.CharField(max_length=10, choices=[(b'S', b'Sedan'), (b'3DH', b'3-door Hatchback'), (b'5DH', b'5-door Hatchback'), (b'C', b'Coupe'), (b'CV', b'Convertible'), (b'SUV', b'SUV'), (b'1CP', b'Single Cabin Pick-Up Truck'), (b'2CP', b'Double Cabin Pick-Up Truck'), (b'O', b'Other')])),
                ('model_name', models.CharField(max_length=200)),
                ('model_year', models.IntegerField()),
                ('engine_type', models.CharField(max_length=300)),
                ('engine_capacity_in_cc', models.IntegerField()),
                ('fuel_type', models.CharField(max_length=20, choices=[(b'NOP', b'Normal Octane Petrol'), (b'HOP', b'High Octane Petrol'), (b'D', b'Diesel'), (b'E', b'Electric'), (b'O', b'Other')])),
                ('drive_type', models.CharField(max_length=100)),
                ('transmission', models.CharField(max_length=100)),
                ('seating_capacity', models.IntegerField()),
                ('mileage_in_kilometres', models.IntegerField()),
                ('color', models.CharField(max_length=100)),
                ('price_in_usd', models.DecimalField(max_digits=12, decimal_places=2)),
                ('description', models.TextField(max_length=1000)),
                ('location', models.CharField(max_length=200)),
                ('is_available', models.BooleanField(default=True)),
                ('is_modified', models.BooleanField(default=False)),
                ('brand', models.ForeignKey(related_name='Car', to='catalog.Brand')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
