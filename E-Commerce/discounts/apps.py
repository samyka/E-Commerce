# -*- coding: utf-8 -*-
# This file is part of E-Commerce.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
import E-Commerce.apps


class AppConfig(E-Commerce.apps.AppConfig):
    name = "E-Commerce.discounts"
    provides = {
        "admin_module": [
            "E-Commerce.discounts.admin.modules.DiscountModule",
            "E-Commerce.discounts.admin.modules.AvailabilityExceptionModule",
            "E-Commerce.discounts.admin.modules.HappyHourModule",
            "E-Commerce.discounts.admin.modules.CouponCodeModule",
        ],
        "discount_module": ["E-Commerce.discounts.modules:ProductDiscountModule"],
        "order_source_modifier_module": ["E-Commerce.discounts.modules:CouponCodeModule"],
        "xtheme_plugin": [
            "E-Commerce.discounts.plugins:DiscountedProductsPlugin"
        ]
    }

    def ready(self):
        import E-Commerce.discounts.signal_handers   # noqa F401
