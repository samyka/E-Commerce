# -*- coding: utf-8 -*-
# This file is part of E-Commerce.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from django.core.urlresolvers import reverse_lazy

from E-Commerce.admin.forms.quick_select import (
    QuickAddRelatedObjectMultiSelect, QuickAddRelatedObjectSelect
)


class QuickAddCouponCodeSelect(QuickAddRelatedObjectSelect):
    url = reverse_lazy("E-Commerce_admin:discounts_coupon_codes.new")


class QuickAddHappyHourMultiSelect(QuickAddRelatedObjectMultiSelect):
    url = reverse_lazy("E-Commerce_admin:discounts_happy_hour.new")


class QuickAddAvailabilityExceptionMultiSelect(QuickAddRelatedObjectMultiSelect):
    url = reverse_lazy("E-Commerce_admin:discounts_availability_exception.new")
