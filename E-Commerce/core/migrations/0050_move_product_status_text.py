# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-28 17:01
from __future__ import unicode_literals

from django.db import migrations, models


def copy_status_text_to_shop_product(apps, schema_editor):
    ProductTranslation = apps.get_model("E-Commerce", "ProductTranslation")
    ShopProduct = apps.get_model("E-Commerce", "ShopProduct")
    ShopProductTranslation = apps.get_model("E-Commerce", "ShopProductTranslation")
    for product_translation in ProductTranslation.objects.all():
        product_id = product_translation.master_id
        for shop_product_id in ShopProduct.objects.filter(product_id=product_id).values_list("id", flat=True):
            trans, _ = ShopProductTranslation.objects.update_or_create(
                master_id=shop_product_id,
                language_code=product_translation.language_code,
                defaults={"status_text": product_translation.status_text}
            )


def copy_status_text_to_product(apps, schema_editor):
    ProductTranslation = apps.get_model("E-Commerce", "ProductTranslation")
    Product = apps.get_model("E-Commerce", "Product")
    ShopProductTranslation = apps.get_model("E-Commerce", "ShopProductTranslation")
    for shop_product_translation in ShopProductTranslation.objects.all():
        shop_product_id = shop_product_translation.master_id
        for product_id in Product.objects.filter(shop_products__id=shop_product_id).values_list("id", flat=True):
            trans, _ = ProductTranslation.objects.update_or_create(
                master_id=product_id,
                language_code=shop_product_translation.language_code,
                defaults={"status_text": shop_product_translation.status_text}
            )


class Migration(migrations.Migration):

    dependencies = [
        ('E-Commerce', '0049_manufacturer_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopproducttranslation',
            name='status_text',
            field=models.CharField(blank=True,
                                   help_text='This text will be shown alongside the product in the shop. It is useful for informing customers of special stock numbers or preorders. (Ex.: "Available in a month")',
                                   max_length=128, verbose_name='status text'),
        ),
        migrations.RunPython(copy_status_text_to_shop_product, copy_status_text_to_product),
        migrations.RemoveField(
            model_name='producttranslation',
            name='status_text',
        )
    ]
