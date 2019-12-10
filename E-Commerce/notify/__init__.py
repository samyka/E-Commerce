# -*- coding: utf-8 -*-
# This file is part of E-Commerce.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.

from E-Commerce.apps import AppConfig


class E-CommerceNotifyAppConfig(AppConfig):
    name = "E-Commerce.notify"
    verbose_name = "E-Commerce Notification Framework"
    label = "E-Commerce_notify"
    provides = {
        "notify_condition": [
            "E-Commerce.notify.conditions:LanguageEqual",
            "E-Commerce.notify.conditions:BooleanEqual",
            "E-Commerce.notify.conditions:IntegerEqual",
            "E-Commerce.notify.conditions:TextEqual",
            "E-Commerce.notify.conditions:Empty",
            "E-Commerce.notify.conditions:NonEmpty",
        ],
        "notify_action": [
            "E-Commerce.notify.actions:SetDebugFlag",
            "E-Commerce.notify.actions:AddOrderLogEntry",
            "E-Commerce.notify.actions:SendEmail",
            "E-Commerce.notify.actions:AddNotification",
        ],
        "notify_event": [],
        "admin_module": [
            "E-Commerce.notify.admin_module:NotifyAdminModule",
        ]
    }


default_app_config = "E-Commerce.notify.E-CommerceNotifyAppConfig"
