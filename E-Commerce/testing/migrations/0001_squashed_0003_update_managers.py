# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models

import E-Commerce.utils.migrations


class Migration(migrations.Migration):
    replaces = [
        ('E-Commerce_testing', '0001_initial'),
        ('E-Commerce_testing', '0002_add_filters'),
        ('E-Commerce_testing', '0003_update_managers'),
    ]

    dependencies = [
        ('E-Commerce', '0001_squashed_0039_alter_names'),
        ('campaigns', '0001_squashed_0011_alter_names'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarrierWithCheckoutPhase',
            fields=[
                ('customcarrier_ptr', models.OneToOneField(
                    serialize=False,
                    to='E-Commerce.CustomCarrier',
                    primary_key=True,
                    parent_link=True,
                    auto_created=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('E-Commerce.customcarrier', ),
            managers = (E-Commerce.utils.migrations.get_managers_for_migration())
        ),
        migrations.CreateModel(
            name='ExpensiveSwedenBehaviorComponent',
            fields=[
                ('servicebehaviorcomponent_ptr', models.OneToOneField(
                    serialize=False,
                    to='E-Commerce.ServiceBehaviorComponent',
                    primary_key=True,
                    parent_link=True,
                    auto_created=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('E-Commerce.servicebehaviorcomponent', )),
        migrations.CreateModel(
            name='PaymentWithCheckoutPhase',
            fields=[
                ('custompaymentprocessor_ptr', models.OneToOneField(
                    serialize=False,
                    to='E-Commerce.CustomPaymentProcessor',
                    primary_key=True,
                    parent_link=True,
                    auto_created=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('E-Commerce.custompaymentprocessor', ),
            managers=(E-Commerce.utils.migrations.get_managers_for_migration())
        ),
        migrations.CreateModel(
            name='PseudoPaymentProcessor',
            fields=[
                ('paymentprocessor_ptr', models.OneToOneField(
                    serialize=False,
                    to='E-Commerce.PaymentProcessor',
                    primary_key=True,
                    parent_link=True,
                    auto_created=True)),
                ('bg_color', models.CharField(
                    blank=True,
                    max_length=20,
                    verbose_name='Payment Page Background Color',
                    default='white')),
                ('fg_color', models.CharField(
                    blank=True,
                    max_length=20,
                    verbose_name='Payment Page Text Color',
                    default='black')),
            ],
            options={
                'abstract': False,
            },
            bases=('E-Commerce.paymentprocessor', ),
            managers=(E-Commerce.utils.migrations.get_managers_for_migration())
        ),
        migrations.CreateModel(
            name='UltraFilter',
            fields=[
                ('catalogfilter_ptr', models.OneToOneField(
                    serialize=False,
                    to='campaigns.CatalogFilter',
                    primary_key=True,
                    parent_link=True,
                    auto_created=True)),
                ('categories', models.ManyToManyField(
                    to='E-Commerce.Category', related_name='ultrafilter2')),
                ('category', models.ForeignKey(
                    to='E-Commerce.Category', null=True,
                    related_name='ultrafilte5')),
                ('contact', models.ForeignKey(null=True, to='E-Commerce.Contact')),
                ('derp', models.ForeignKey(
                    to='E-Commerce.Category',
                    null=True,
                    related_name='ultrafilte55')),
                ('product', models.ForeignKey(null=True, to='E-Commerce.Product')),
                ('product_type', models.ForeignKey(
                    null=True, to='E-Commerce.ProductType')),
                ('product_types', models.ManyToManyField(
                    to='E-Commerce.ProductType', related_name='ultrafilter3')),
                ('products', models.ManyToManyField(
                    to='E-Commerce.Product', related_name='ultrafilter1')),
                ('shop_product', models.ForeignKey(
                    null=True, to='E-Commerce.ShopProduct')),
                ('shop_products', models.ManyToManyField(
                    to='E-Commerce.ShopProduct', related_name='ultrafilter4')),
            ],
            options={
                'abstract': False,
            },
            bases=('campaigns.catalogfilter', )),
    ]
