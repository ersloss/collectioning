# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-02 15:45
from __future__ import unicode_literals

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0009_auto_20170226_1444'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='price',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10),
        ),
    ]
