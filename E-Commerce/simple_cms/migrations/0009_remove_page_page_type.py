# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-06-22 19:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('E-Commerce_simple_cms', '0008_page_show_child_timestamps'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='page_type',
        ),
    ]