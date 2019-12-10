# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0003_category_products'),
        ('E-Commerce', '0004_update_orderline_refunds'),
        ('E-Commerce_testing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UltraFilter',
            fields=[
                ('catalogfilter_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='campaigns.CatalogFilter')),
                ('categories', models.ManyToManyField(related_name='ultrafilter2', to='E-Commerce.Category')),
                ('category', models.ForeignKey(related_name='ultrafilte5', to='E-Commerce.Category', null=True)),
                ('contact', models.ForeignKey(to='E-Commerce.Contact', null=True)),
                ('derp', models.ForeignKey(related_name='ultrafilte55', to='E-Commerce.Category', null=True)),
                ('product', models.ForeignKey(to='E-Commerce.Product', null=True)),
                ('product_type', models.ForeignKey(to='E-Commerce.ProductType', null=True)),
                ('product_types', models.ManyToManyField(related_name='ultrafilter3', to='E-Commerce.ProductType')),
                ('products', models.ManyToManyField(related_name='ultrafilter1', to='E-Commerce.Product')),
                ('shop_product', models.ForeignKey(to='E-Commerce.ShopProduct', null=True)),
                ('shop_products', models.ManyToManyField(related_name='ultrafilter4', to='E-Commerce.ShopProduct')),
            ],
            options={
                'abstract': False,
            },
            bases=('campaigns.catalogfilter',),
        ),
    ]
