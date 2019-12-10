# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-01-30 19:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('E-Commerce', '0029_personcontact_names'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(db_index=True, editable=False, verbose_name='order date'),
        ),
        migrations.AlterField(
            model_name='product',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='created on'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='modified_on',
            field=models.DateTimeField(auto_now=True, db_index=True, verbose_name='modified on'),
        )
    ]
