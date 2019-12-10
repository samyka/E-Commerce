# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import E-Commerce.utils.properties
import E-Commerce.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('E-Commerce', '0051_supplier_enabled'),
        ('E-Commerce_testing', '0004_fieldsmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='SupplierPrice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('amount_value', E-Commerce.core.fields.MoneyValueField(max_digits=36, decimal_places=9)),
                ('product', models.ForeignKey(to='E-Commerce.Product')),
                ('shop', models.ForeignKey(to='E-Commerce.Shop')),
                ('supplier', models.ForeignKey(to='E-Commerce.Supplier')),
            ],
            bases=(E-Commerce.utils.properties.MoneyPropped, models.Model),
        ),
    ]
