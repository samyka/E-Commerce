# This file is part of E-Commerce.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
import pytest

from django.test import override_settings

from E-Commerce.core import cache
from E-Commerce.core.models import Manufacturer
from E-Commerce.front.forms.product_list_modifiers import (
    ManufacturerProductListFilter
)

from E-Commerce.testing import factories
from E-Commerce.testing.utils import apply_request_middleware


@pytest.mark.django_db
def test_manufacturer_filter_get_fields(rf):
    cache.clear()

    shop = factories.get_default_shop()

    request = apply_request_middleware(rf.get("/"))
    assert ManufacturerProductListFilter().get_fields(request, None) is None

    manufacturer = Manufacturer.objects.create(name="Random Brand Inc")
    assert ManufacturerProductListFilter().get_fields(request, None) is None

    category = factories.get_default_category()
    product = factories.create_product("sku", shop=shop)
    shop_product = product.get_shop_instance(shop=shop)
    shop_product.primary_category = category
    shop_product.save()

    assert ManufacturerProductListFilter().get_fields(request, category) is None

    # Now once we link manufacturer to product we should get
    # form field for manufacturer
    product.manufacturer = manufacturer
    product.save()
    form_field = ManufacturerProductListFilter().get_fields(request, category)[0][1]
    assert form_field is not None
    assert form_field.label == "Manufacturers"

    with override_settings(E-Commerce_FRONT_OVERRIDE_SORTS_AND_FILTERS_LABELS_LOGIC={"manufacturers": "Brands"}):
        form_field = ManufacturerProductListFilter().get_fields(request, category)[0][1]
        assert form_field is not None
        assert form_field.label == "Brands"
