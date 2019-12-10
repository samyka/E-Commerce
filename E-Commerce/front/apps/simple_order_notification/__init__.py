# -*- coding: utf-8 -*-
# This file is part of E-Commerce.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from E-Commerce.apps import AppConfig


class SimpleOrderNotificationAppConfig(AppConfig):
    name = "E-Commerce.front.apps.simple_order_notification"
    verbose_name = "E-Commerce Frontend - Simple Order Notification"
    label = "E-Commerce_front.simple_order_notification"

    provides = {
        "admin_module": [
            "E-Commerce.front.apps.simple_order_notification.admin_module:SimpleOrderNotificationModule",
        ]
    }


default_app_config = "E-Commerce.front.apps.simple_order_notification.SimpleOrderNotificationAppConfig"
