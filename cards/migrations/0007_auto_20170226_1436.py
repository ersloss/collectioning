# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-26 19:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0006_auto_20170226_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='name',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='card',
            name='type',
            field=models.CharField(max_length=150),
        ),
    ]
