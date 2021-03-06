# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models, connection


def combine_refund_types(apps, schema_editor):
    # convert AMOUNT_REFUND (8) to REFUND (6)
    with connection.cursor() as c:
        c.execute("UPDATE E-Commerce_orderline SET type = 6 WHERE type = 8")


class Migration(migrations.Migration):

    dependencies = [
        ('E-Commerce', '0003_shopproduct_backorder_maximum'),
    ]

    operations = [
        migrations.RunPython(combine_refund_types),
    ]
