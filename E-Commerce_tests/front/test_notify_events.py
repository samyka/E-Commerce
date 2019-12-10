# -*- coding: utf-8 -*-
# This file is part of E-Commerce.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from __future__ import unicode_literals

from datetime import datetime

import mock
import pytest
import pytz

from E-Commerce.core.models import OrderStatus, OrderStatusManager
from E-Commerce.notify.models import Script
from E-Commerce.testing import factories
from E-Commerce.utils.i18n import get_locally_formatted_datetime


@pytest.mark.django_db
def test_class_refunded():
    shop = factories.get_default_shop()
    supplier = factories.get_default_supplier()
    customer = factories.create_random_person("en")
    OrderStatusManager().ensure_default_statuses()

    product = factories.create_product("p", shop, supplier, 1.0)
    order = factories.create_order_with_product(product, supplier, 1, 1, shop=shop)

    # make sure to have some script enabled
    Script.objects.create(shop=shop, event_identifier="order_status_changed", name="Script", enabled=True)

    def get_mocked_cls():
        return mock.MagicMock(identifier="order_status_changed")

    with mock.patch("E-Commerce.front.notify_events.OrderStatusChanged", new_callable=get_mocked_cls) as mocked:
        order.status = OrderStatus.objects.get_default_processing()
        order.save()
        mocked.assert_called()
        order.refresh_from_db()
        assert mocked.call_args.kwargs["order"] == order
        assert mocked.call_args.kwargs["old_status"] == OrderStatus.objects.get_default_initial()
        assert mocked.call_args.kwargs["new_status"] == OrderStatus.objects.get_default_processing()
        assert order.status == OrderStatus.objects.get_default_processing()

    # nothing changes
    with mock.patch("E-Commerce.front.notify_events.OrderStatusChanged", new_callable=get_mocked_cls) as mocked:
        order.status = OrderStatus.objects.get_default_processing()
        order.save()
        mocked.assert_not_called()
