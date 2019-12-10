# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-12-14 10:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('default_tax', '0002_postal_code_pattern_to_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taxrule',
            name='customer_tax_groups',
            field=models.ManyToManyField(blank=True, help_text='The customer tax groups for which this tax rule is limited.', to='E-Commerce.CustomerTaxGroup', verbose_name='customer tax groups'),
        ),
        migrations.AlterField(
            model_name='taxrule',
            name='enabled',
            field=models.BooleanField(db_index=True, default=True, help_text='Check this if this tax rule is active.', verbose_name='enabled'),
        ),
        migrations.AlterField(
            model_name='taxrule',
            name='tax',
            field=models.ForeignKey(help_text='The tax to apply when this rule is applied.', on_delete=django.db.models.deletion.PROTECT, to='E-Commerce.Tax', verbose_name='tax'),
        ),
    ]
