# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-26 19:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0004_auto_20170226_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='power',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='toughness',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]