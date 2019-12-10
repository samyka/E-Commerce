# -*- coding: utf-8 -*-
# This file is part of E-Commerce.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from __future__ import unicode_literals

from decimal import Decimal

import pytest
from django.test.utils import override_settings

from E-Commerce.apps.provides import override_provides
from E-Commerce.core.models import MutableAddress, OrderLineType
from E-Commerce.core.order_creator import OrderSource, SourceLine
from E-Commerce.core.pricing import TaxfulPrice, TaxlessPrice
from E-Commerce.core.taxing import TaxModule
from E-Commerce.core.taxing.utils import stacked_value_added_taxes
from E-Commerce.testing.factories import get_shop, get_tax

TAX_MODULE_SPEC = [__name__ + ":IrvineCaliforniaTaxation"]


class IrvineCaliforniaTaxation(TaxModule):
    identifier = "irvine"

    def get_taxed_price(self, context, price, tax_class):
        taxes = []
        if context.postal_code == "92602":
            taxes = [
                # Based on data from TaxJar
                get_tax("CA", "California", rate="0.065"),
                get_tax("CA-OC", "Orange County", rate="0.01"),
                get_tax("CA-OC-IR", "Irvine", rate="0.00"),
                get_tax("CA-OC-IR-DS", "District tax", rate="0.005"),
            ]
        return stacked_value_added_taxes(price, taxes)

    def _add_proportional_taxes(self, context, tax_class_proportions, lines):
        for line in lines:
            line.taxes = self.get_taxed_price(context, line.price, None).taxes


@pytest.mark.django_db
def test_stacked_tax_taxless_price():
    source = OrderSource(get_shop(prices_include_tax=False))
    assert source.prices_include_tax is False
    source.add_line(
        type=OrderLineType.OTHER, quantity=1, base_unit_price=source.create_price(10)
    )
    with override_provides("tax_module", TAX_MODULE_SPEC):
        with override_settings(E-Commerce_TAX_MODULE="irvine"):
            source.shipping_address = MutableAddress(
                street="16215 Alton Pkwy",
                postal_code="92602",
            )
            line = source.get_final_lines(with_taxes=True)[0]
            assert isinstance(line, SourceLine)
            assert line.taxes
            assert line.taxful_price.value == Decimal("10.800")
            source.uncache()

            # Let's move out to a taxless location.
            source.shipping_address.postal_code = "11111"
            line = source.get_final_lines(with_taxes=True)[0]
            assert isinstance(line, SourceLine)
            assert not line.taxes
            assert line.taxful_price.value == Decimal("10")


@pytest.mark.django_db
def test_stacked_tax_taxful_price():
    shop = get_shop(prices_include_tax=True, currency='EUR')
    source = OrderSource(shop)
    assert source.prices_include_tax
    source.add_line(
        type=OrderLineType.OTHER, quantity=1, base_unit_price=source.create_price(20)
    )
    with override_provides("tax_module", TAX_MODULE_SPEC):
        with override_settings(E-Commerce_TAX_MODULE="irvine"):
            source.shipping_address = MutableAddress(
                street="16215 Alton Pkwy",
                postal_code="92602",
            )
            line = source.get_final_lines(with_taxes=True)[0]
            assert isinstance(line, SourceLine)
            assert line.taxes
            assert line.taxful_price == TaxfulPrice(20, 'EUR')
            assert_almost_equal(line.taxless_price, TaxlessPrice("18.52", 'EUR'))
            source.uncache()

            # Let's move out to a taxless location.
            source.shipping_address.postal_code = "11111"
            line = source.get_final_lines(with_taxes=True)[0]
            assert isinstance(line, SourceLine)
            assert not line.taxes
            assert line.taxful_price == TaxfulPrice(20, source.currency)
            assert line.taxless_price.value == Decimal("20")


def assert_almost_equal(x, y):
    assert Decimal(abs(x - y)) < 0.00001
