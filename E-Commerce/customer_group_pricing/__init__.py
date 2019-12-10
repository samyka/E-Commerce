# -*- coding: utf-8 -*-
# This file is part of E-Commerce.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from django.utils.translation import ugettext_lazy as _

import E-Commerce.apps


# TODO: Document how to create custom pricing modules (Refs E-Commerce-514)
class CustomerGroupPricingAppConfig(E-Commerce.apps.AppConfig):
    name = __name__
    verbose_name = _("E-Commerce Customer Group Pricing")
    label = "E-Commerce_customer_group_pricing"
    provides = {
        "pricing_module": [
            __name__ + ".module:CustomerGroupPricingModule"
        ],
        "discount_module": [
            __name__ + ".module:CustomerGroupDiscountModule"
        ],
        "admin_product_form_part": [
            __name__ + ".admin_form_part:CustomerGroupPricingFormPart",
            __name__ + ".admin_form_part:CustomerGroupPricingDiscountFormPart"
        ],
        "api_populator": [
            __name__ + ".api:populate_customer_group_pricing_api"
        ]
    }

    def ready(self):
        # connect signals
        import E-Commerce.customer_group_pricing.signal_handers    # noqa F401


default_app_config = __name__ + ".CustomerGroupPricingAppConfig"
