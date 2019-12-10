# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import E-Commerce.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('E-Commerce', '0002_rounding'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopproduct',
            name='backorder_maximum',
            field=E-Commerce.core.fields.QuantityField(verbose_name='backorder maximum', null=True, default=0, max_digits=36, blank=True, decimal_places=9),
        ),
    ]
