# -*- coding: utf-8 -*-
# This file is part of E-Commerce.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
import json

import pytest

from django.test import override_settings

from E-Commerce.core.settings import E-Commerce_ENABLE_MULTIPLE_SUPPLIERS
from E-Commerce.testing import factories
from E-Commerce.testing.utils import apply_request_middleware
from E-Commerce.utils.importing import load


@pytest.mark.django_db
def test_list_view(rf, admin_user):
    shop = factories.get_default_shop()

    product = factories.create_product(sku="test", shop=shop)
    shop_product = product.get_shop_instance(shop)
    shop_product.primary_category = factories.get_default_category()
    shop_product.save()
    shop_product.categories.add(shop_product.primary_category)

    view = load("E-Commerce.admin.modules.products.views:ProductListView").as_view()
    request = apply_request_middleware(rf.get("/", {
        "jq": json.dumps({"perPage": 100, "page": 1})
    }), user=admin_user)
    response = view(request)
    assert 200 <= response.status_code < 300

    data = json.loads(response.content.decode("utf-8"))
    product_data = [item for item in data["items"] if item["_id"] == shop_product.pk][0]
    assert product_data["primary_category"] == factories.get_default_category().name
    assert product_data["categories"] == factories.get_default_category().name
    assert product_data["categories"] == factories.get_default_category().name

    # Suppliers not available by default since multiple suppliers is not enabled
    assert "suppliers" not in product_data


@pytest.mark.django_db
def test_list_view_with_multiple_suppliers(rf, admin_user):
    shop = factories.get_default_shop()

    product = factories.create_product(sku="test", shop=shop)
    shop_product = product.get_shop_instance(shop)
    shop_product.primary_category = factories.get_default_category()
    shop_product.save()
    shop_product.categories.add(shop_product.primary_category)

    # Also one product with supplier
    supplier = factories.get_default_supplier()
    product2 = factories.create_product(sku="test2", shop=shop, supplier=supplier)
    shop_product2 = product2.get_shop_instance(shop)
    shop_product2.primary_category = factories.get_default_category()
    shop_product2.save()
    shop_product2.categories.add(shop_product.primary_category)

    with override_settings(E-Commerce_ENABLE_MULTIPLE_SUPPLIERS=True):
        view = load("E-Commerce.admin.modules.products.views:ProductListView").as_view()
        request = apply_request_middleware(rf.get("/", {
            "jq": json.dumps({"perPage": 100, "page": 1})
        }), user=admin_user)
        response = view(request)
        assert 200 <= response.status_code < 300

        data = json.loads(response.content.decode("utf-8"))
        product_data = [item for item in data["items"] if item["_id"] == shop_product.pk][0]
        assert product_data["primary_category"] == factories.get_default_category().name
        assert product_data["categories"] == factories.get_default_category().name
        assert product_data["categories"] == factories.get_default_category().name
        assert product_data["suppliers"] == ""

        product_data2 = [item for item in data["items"] if item["_id"] == shop_product2.pk][0]
        assert product_data2["suppliers"] == factories.get_default_supplier().name
