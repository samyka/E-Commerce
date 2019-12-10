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
from E-Commerce.discounts.models import Discount


class DiscountModule(AdminModule):
    name = _("Discounts")
    breadcrumbs_menu_entry = MenuEntry(name, url="E-Commerce_admin:discounts.list")

    def get_urls(self):
        from E-Commerce.admin.urls import admin_url
        archive = admin_url(
            "^archived_discounts",
            "E-Commerce.discounts.admin.views.ArchivedDiscountListView",
            name="discounts.archive"
        )

        delete = admin_url(
            "^discounts/(?P<pk>\d+)/delete/$",
            "E-Commerce.discounts.admin.views.DiscountDeleteView",
            name="discounts.delete"
        )

        return [archive, delete] + get_edit_and_list_urls(
            url_prefix="^discounts",
            view_template="E-Commerce.discounts.admin.views.Discount%sView",
            name_template="discounts.%s"
        )

    def get_menu_entries(self, request):
        return [
            MenuEntry(
                text=_("Product Discounts"),
                icon="fa fa-percent",
                url="E-Commerce_admin:discounts.list",
                category=CAMPAIGNS_MENU_CATEGORY,
                ordering=4
            ),
            MenuEntry(
                text=_("Archived Product Discounts"),
                icon="fa fa-percent",
                url="E-Commerce_admin:discounts.archive",
                category=CAMPAIGNS_MENU_CATEGORY,
                ordering=5
            )
        ]

    def get_model_url(self, object, kind, shop=None):
        return derive_model_url(Discount, "E-Commerce_admin:discounts", object, kind)
