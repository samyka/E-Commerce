# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-05-09 17:24
from __future__ import unicode_literals

from django.db import migrations
import E-Commerce.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('E-Commerce', '0058_make_product_type_nullable'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='options',
            field=E-Commerce.core.fields.PolymorphicJSONField(blank=True, null=True, verbose_name='options'),
        ),
    ]
