# -*- coding: utf-8 -*-
# This file is part of E-Commerce.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from __future__ import unicode_literals

from E-Commerce.admin.forms import E-CommerceAdminForm
from E-Commerce.core.models import CustomCarrier, CustomPaymentProcessor


class CustomCarrierForm(E-CommerceAdminForm):
    class Meta:
        model = CustomCarrier
        exclude = ("identifier", )


class CustomPaymentProcessorForm(E-CommerceAdminForm):
    class Meta:
        model = CustomPaymentProcessor
        exclude = ("identifier", )
