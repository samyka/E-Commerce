# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import E-Commerce.utils.properties
import E-Commerce.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('E-Commerce', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CgpPrice',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('price_value', E-Commerce.core.fields.MoneyValueField(verbose_name='price', decimal_places=9, max_digits=36)),
                ('group', models.ForeignKey(verbose_name='contact group', to='E-Commerce.ContactGroup')),
                ('product', models.ForeignKey(related_name='+', to='E-Commerce.Product', verbose_name='product')),
                ('shop', models.ForeignKey(verbose_name='shop', to='E-Commerce.Shop')),
            ],
            options={
                'verbose_name': 'product price',
                'verbose_name_plural': 'product prices',
            },
            bases=(E-Commerce.utils.properties.MoneyPropped, models.Model),
        ),
        migrations.AlterUniqueTogether(
            name='cgpprice',
            unique_together=set([('product', 'shop', 'group')]),
        ),
    ]
