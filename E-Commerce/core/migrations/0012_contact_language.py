# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-11-04 17:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('E-Commerce', '0011_remove_product_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='language',
            new_name='_language',
        ),
    ]
