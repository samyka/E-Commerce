# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-04-11 23:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('E-Commerce', '0028_displayunit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personcontact',
            name='first_name',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='personcontact',
            name='last_name',
            field=models.CharField(blank=True, max_length=120),
        ),
    ]
