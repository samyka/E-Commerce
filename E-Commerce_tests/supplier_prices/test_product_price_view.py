# -*- coding: utf-8 -*-
# This file is part of E-Commerce.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from __future__ import unicode_literals

import pytest
from bs4 import BeautifulSoup
from django.core.urlresolvers import reverse
from django.test import override_settings

from E-Commerce.core.models import Supplier
from E-Commerce.testing import factories
from E-Commerce.testing.models import SupplierPrice


@pytest.mark.django_db
def test_product_price(client):
    shop = factories.get_default_shop()
    product = factories.create_product("sku", shop=shop, default_price=30)
    shop_product = product.get_shop_instance(shop)

    supplier_data = [
        ("Johnny Inc", 30),
        ("Mike Inc", 20),
        ("Simon Inc", 10),
    ]
    for name, product_price in supplier_data:
        supplier = Supplier.objects.create(name=name)
        shop_product.suppliers.add(supplier)
        SupplierPrice.objects.create(supplier=supplier, shop=shop, product=product, amount_value=product_price)

    strategy = "E-Commerce.testing.supplier_pricing.supplier_strategy:CheapestSupplierPriceSupplierStrategy"
    with override_settings(E-Commerce_PRICING_MODULE="supplier_pricing", E-Commerce_SHOP_PRODUCT_SUPPLIERS_STRATEGY=strategy):
        for name, price in supplier_data:
            supplier = Supplier.objects.get(name=name)
            response = client.get(
                reverse('E-Commerce:xtheme_extra_view', kwargs={
                        'view': 'product_price'
                    }
                ) + "?id=%s&quantity=%s&supplier=%s" % (product.pk, 1, supplier.pk)
            )
            soup = BeautifulSoup(response.content)
            price_span = soup.find("span", {"class": "product-price"})
            assert "%s" % price in price_span.text
