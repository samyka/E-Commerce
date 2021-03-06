# -*- coding: utf-8 -*-
# This file is part of E-Commerce.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _

from E-Commerce.admin.shop_provider import get_shop
from E-Commerce.discounts.models import Discount

from ._active_list import DiscountListView


class ArchivedDiscountListView(DiscountListView):

    mass_actions = [
        "E-Commerce.discounts.admin.mass_actions:UnarchiveMassAction",
        "E-Commerce.discounts.admin.mass_actions:DeleteMassAction"
    ]

    def get_queryset(self):
        return Discount.objects.archived(get_shop(self.request))

    def get_context_data(self, **kwargs):
        context = super(ArchivedDiscountListView, self).get_context_data(**kwargs)
        context["title"] = _("Archived Product Discounts")
        return context
