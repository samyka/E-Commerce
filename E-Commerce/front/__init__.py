# -*- coding: utf-8 -*-
# This file is part of E-Commerce.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from E-Commerce.apps import AppConfig
from E-Commerce.apps.settings import validate_templates_configuration


class E-CommerceFrontAppConfig(AppConfig):
    name = "E-Commerce.front"
    verbose_name = "E-Commerce Frontend"
    label = "E-Commerce_front"

    provides = {
        "admin_category_form_part": [
            "E-Commerce.front.admin_module.sorts_and_filters.form_parts.ConfigurationCategoryFormPart"
        ],
        "admin_module": [
            "E-Commerce.front.admin_module.CartAdminModule",
        ],
        "admin_shop_form_part": [
            "E-Commerce.front.admin_module.sorts_and_filters.form_parts.ConfigurationShopFormPart",
            "E-Commerce.front.admin_module.checkout.form_parts.CheckoutShopFormPart",
            "E-Commerce.front.admin_module.companies.form_parts.RegistrationSettingsFormPart",
            "E-Commerce.front.admin_module.translation.form_parts.TranslationSettingsFormPart",
            "E-Commerce.front.admin_module.carts.form_parts.CartDelayFormPart"
        ],
        "notify_event": [
            "E-Commerce.front.notify_events:OrderReceived",
            "E-Commerce.front.notify_events:OrderStatusChanged",
            "E-Commerce.front.notify_events:ShipmentCreated",
            "E-Commerce.front.notify_events:ShipmentDeleted",
            "E-Commerce.front.notify_events:PaymentCreated",
            "E-Commerce.front.notify_events:RefundCreated",
        ],
        "notify_script_template": [
            "E-Commerce.front.notify_script_templates:PaymentCreatedEmailScriptTemplate",
            "E-Commerce.front.notify_script_templates:RefundCreatedEmailScriptTemplate",
            "E-Commerce.front.notify_script_templates:ShipmentDeletedEmailScriptTemplate",
            "E-Commerce.front.notify_script_templates:OrderConfirmationEmailScriptTemplate",
            "E-Commerce.front.notify_script_templates:ShipmentCreatedEmailScriptTemplate",
        ],
        "front_extend_product_list_form": [
            "E-Commerce.front.forms.product_list_modifiers.CategoryProductListFilter",
            "E-Commerce.front.forms.product_list_modifiers.LimitProductListPageSize",
            "E-Commerce.front.forms.product_list_modifiers.ProductPriceFilter",
            "E-Commerce.front.forms.product_list_modifiers.ProductVariationFilter",
            "E-Commerce.front.forms.product_list_modifiers.SortProductListByCreatedDate",
            "E-Commerce.front.forms.product_list_modifiers.SortProductListByAscendingCreatedDate",
            "E-Commerce.front.forms.product_list_modifiers.SortProductListByName",
            "E-Commerce.front.forms.product_list_modifiers.SortProductListByPrice",
            "E-Commerce.front.forms.product_list_modifiers.ManufacturerProductListFilter",
            "E-Commerce.front.forms.product_list_supplier_modifier.SupplierProductListFilter"
        ],
        "front_product_order_form": [
            "E-Commerce.front.forms.order_forms:VariableVariationProductOrderForm",
            "E-Commerce.front.forms.order_forms:SimpleVariationProductOrderForm",
            "E-Commerce.front.forms.order_forms:SimpleProductOrderForm",
        ],
        "front_model_url_resolver": [
            "E-Commerce.front.utils.urls.model_url"
        ]
    }

    def ready(self):
        # connect signals
        import E-Commerce.front.notify_events  # noqa: F401
        import E-Commerce.front.signal_handlers  # noqa: F401
        validate_templates_configuration()


default_app_config = "E-Commerce.front.E-CommerceFrontAppConfig"
