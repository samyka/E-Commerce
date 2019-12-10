# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models

import E-Commerce.core.fields
import E-Commerce.utils.properties


class Migration(migrations.Migration):

    replaces = [
        ('E-Commerce_customer_group_pricing', '0001_initial'),
        ('E-Commerce_customer_group_pricing', '0002_discounts'),
    ]

    dependencies = [
        ('E-Commerce', '0001_squashed_0039_alter_names'),
    ]

    operations = [
        migrations.CreateModel(
            name='CgpPrice',
            fields=[
                ('id', models.AutoField(
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID',
                    auto_created=True)),
                ('price_value', E-Commerce.core.fields.MoneyValueField(
                    max_digits=36, decimal_places=9, verbose_name='price')),
                ('group', models.ForeignKey(
                    to='E-Commerce.ContactGroup', verbose_name='contact group')),
                ('product', models.ForeignKey(
                    related_name='+',
                    verbose_name='product',
                    to='E-Commerce.Product')),
                ('shop', models.ForeignKey(
                    to='E-Commerce.Shop', verbose_name='shop')),
            ],
            options={
                'verbose_name_plural': 'product prices',
                'verbose_name': 'product price',
            },
            bases=(E-Commerce.utils.properties.MoneyPropped, models.Model), ),
        migrations.AlterUniqueTogether(
            name='cgpprice',
            unique_together=set([('product', 'shop', 'group')]), ),
        migrations.CreateModel(
            name='CgpDiscount',
            fields=[
                ('id', models.AutoField(
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID',
                    auto_created=True)),
                ('discount_amount_value', E-Commerce.core.fields.MoneyValueField(
                    max_digits=36,
                    decimal_places=9,
                    verbose_name='discount amount')),
                ('group', models.ForeignKey(
                    to='E-Commerce.ContactGroup', verbose_name='contact group')),
                ('product', models.ForeignKey(
                    related_name='+',
                    verbose_name='product',
                    to='E-Commerce.Product')),
                ('shop', models.ForeignKey(
                    to='E-Commerce.Shop', verbose_name='shop')),
            ],
            options={
                'verbose_name_plural': 'product discounts',
                'abstract': False,
                'verbose_name': 'product discount',
            },
            bases=(E-Commerce.utils.properties.MoneyPropped, models.Model), ),
        migrations.AlterUniqueTogether(
            name='cgpdiscount',
            unique_together=set([('product', 'shop', 'group')]), ),
    ]
