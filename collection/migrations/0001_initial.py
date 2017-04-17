# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-16 23:59
from __future__ import unicode_literals

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cards', '0010_card_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('total_value', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=30)),
                ('cards', models.ManyToManyField(to='cards.Card')),
            ],
        ),
    ]
