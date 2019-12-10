# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import enumfields.fields
import E-Commerce.core.suppliers.enums


class Migration(migrations.Migration):

    dependencies = [
        ('simple_supplier', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stockadjustment',
            name='type',
            field=enumfields.fields.EnumIntegerField(default=1, db_index=True, verbose_name='type', enum=E-Commerce.core.suppliers.enums.StockAdjustmentType),
        ),
    ]
