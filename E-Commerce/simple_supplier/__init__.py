# -*- coding: utf-8 -*-
# This file is part of E-Commerce.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from E-Commerce.apps import AppConfig


class E-CommerceSimpleSupplierAppConfig(AppConfig):
    name = "E-Commerce.simple_supplier"
    verbose_name = "E-Commerce Simple Supplier"
    label = "simple_supplier"
    provides = {
        "supplier_module": [
            "E-Commerce.simple_supplier.module:SimpleSupplierModule"
        ],
        "admin_product_form_part": [
            "E-Commerce.simple_supplier.admin_module.forms:SimpleSupplierFormPart"
        ],
        "admin_module": [
            "E-Commerce.simple_supplier.admin_module:StocksAdminModule"
        ],
        "notify_event": [
            "E-Commerce.simple_supplier.notify_events:AlertLimitReached"
        ],
        "notify_script_template": [
            "E-Commerce.simple_supplier.notify_script_template:StockLimitEmailScriptTemplate",
        ]
    }


default_app_config = "E-Commerce.simple_supplier.E-CommerceSimpleSupplierAppConfig"
