# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-11-08 20:33
from __future__ import unicode_literals

import enumfields.fields
import E-Commerce.core.models
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.db import migrations, models


def forwards_func(apps, schema_editor):
    OrderStatus = apps.get_model("E-Commerce", "OrderStatus")
    OrderStatusTranslation = apps.get_model("E-Commerce", "OrderStatusTranslation")

    for object in OrderStatus.objects.all():
        for language_code in OrderStatusTranslation.objects.all().values_list("language_code", flat=True).distinct():
            translation = _get_translation(object, OrderStatusTranslation, language_code=language_code)
            if translation:
                trans, _ = OrderStatusTranslation.objects.update_or_create(
                    master_id=object.pk,
                    language_code=language_code,
                    defaults={"public_name": translation.name}
                )


def _get_translation(object, MyModelTranslation, language_code):
    translations = MyModelTranslation.objects.filter(master_id=object.pk)
    try:
        # Try default translation
        return translations.get(language_code=language_code)
    except ObjectDoesNotExist:
        return None


def backwards_func(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('E-Commerce', '0013_product_shipping_mode_default'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderstatus',
            name='is_active',
            field=models.BooleanField(db_index=True, default=True, help_text='Define if the status is usable.', verbose_name='is active'),
        ),
        migrations.AddField(
            model_name='orderstatustranslation',
            name='public_name',
            field=models.CharField(default='status', help_text='The name shown for customer in shop front.', max_length=64, verbose_name='public name'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='orderstatus',
            name='default',
            field=models.BooleanField(db_index=True, default=False, help_text='Defines if the status should be considered as default.', verbose_name='default'),
        ),
        migrations.AlterField(
            model_name='orderstatus',
            name='ordering',
            field=models.IntegerField(db_index=True, default=0, help_text='The processing order of statuses. Default is always processed first.', verbose_name='ordering'),
        ),
        migrations.AlterField(
            model_name='orderstatus',
            name='role',
            field=enumfields.fields.EnumIntegerField(db_index=True, default=0, enum=E-Commerce.core.models.OrderStatusRole, help_text='Role of status. One role can have multiple order statuses.', verbose_name='role'),
        ),
        migrations.AlterField(
            model_name='orderstatustranslation',
            name='name',
            field=models.CharField(help_text='Name of the order status', max_length=64, verbose_name='name'),
        ),
        migrations.AlterModelOptions(
            name='orderstatus',
            options={'verbose_name': 'order status', 'verbose_name_plural': 'order statuses'},
        ),
        migrations.AlterUniqueTogether(
            name='orderstatus',
            unique_together=set([('identifier', 'role')]),
        ),
        migrations.RunPython(forwards_func, backwards_func)
    ]
