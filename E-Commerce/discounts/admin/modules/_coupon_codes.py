# -*- coding: utf-8 -*-
# This file is part of E-Commerce.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _

from E-Commerce.admin.base import AdminModule, MenuEntry
from E-Commerce.admin.menu import CAMPAIGNS_MENU_CATEGORY
from E-Commerce.admin.utils.urls import derive_model_url, get_edit_and_list_urls
from E-Commerce.discounts.models import CouponCode


class CouponCodeModule(AdminModule):
    name = _("Product Discounts Coupon Codes")
    breadcrumbs_menu_entry = MenuEntry(name, url="E-Commerce_admin:discounts_coupon_codes.list")

    def get_urls(self):
        from E-Commerce.admin.urls import admin_url
        delete = admin_url(
            "^discounts_coupon_codes/(?P<pk>\d+)/delete/$",
            "E-Commerce.discounts.admin.views.CouponCodeDeleteView",
            name="discounts_coupon_codes.delete"
        )

        return [delete] + get_edit_and_list_urls(
            url_prefix="^discounts_coupon_codes",
            view_template="E-Commerce.discounts.admin.views.CouponCode%sView",
            name_template="discounts_coupon_codes.%s"
        )

    def get_menu_entries(self, request):
        return [
            MenuEntry(
                text=_("Product Discounts Coupon Codes"),
                icon="fa fa-percent",
                url="E-Commerce_admin:discounts_coupon_codes.list",
                category=CAMPAIGNS_MENU_CATEGORY,
                ordering=8
            )
        ]

    def get_model_url(self, object, kind, shop=None):
        return derive_model_url(CouponCode, "E-Commerce_admin:discounts_coupon_codes", object, kind)
