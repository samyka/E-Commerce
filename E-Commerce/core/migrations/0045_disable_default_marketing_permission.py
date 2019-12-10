# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-05-25 14:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('E-Commerce', '0044_add_media'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='marketing_permission',
            field=models.BooleanField(default=False, help_text='Check this if the contact can receive marketing and promotional materials.', verbose_name='marketing permission'),
        ),
        migrations.AlterField(
            model_name='order',
            name='marketing_permission',
            field=models.BooleanField(default=False, verbose_name='marketing permission'),
        ),
    ]
