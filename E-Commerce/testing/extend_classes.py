# -*- coding: utf-8 -*-
# This file is part of E-Commerce.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from E-Commerce.core.models import ProductMode
from E-Commerce.front.forms.order_forms import ProductOrderForm


class DifferentProductOrderForm(ProductOrderForm):
    template_name = "E-Commerce_testing/different_order_form.jinja"

    def is_compatible(self):
        return (self.product.mode == ProductMode.SUBSCRIPTION)
