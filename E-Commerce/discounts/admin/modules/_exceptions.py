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
from E-Commerce.discounts.models import AvailabilityException


class AvailabilityExceptionModule(AdminModule):
    name = _("Discounts Availability Exceptions")
    breadcrumbs_menu_entry = MenuEntry(name, url="E-Commerce_admin:discounts_availability_exception.list")

    def get_urls(self):
        from E-Commerce.admin.urls import admin_url
        delete = admin_url(
            "^discounts_availability_exception/(?P<pk>\d+)/delete/$",
            "E-Commerce.discounts.admin.views.AvailabilityExceptionDeleteView",
            name="discounts_availability_exception.delete"
        )

        return [delete] + get_edit_and_list_urls(
            url_prefix="^discounts_availability_exception",
            view_template="E-Commerce.discounts.admin.views.AvailabilityException%sView",
            name_template="discounts_availability_exception.%s"
        )

    def get_menu_entries(self, request):
        return [
            MenuEntry(
                text=_("Product Discounts Availability Exceptions"),
                icon="fa fa-percent",
                url="E-Commerce_admin:discounts_availability_exception.list",
                category=CAMPAIGNS_MENU_CATEGORY,
                ordering=6
            )
        ]

    def get_model_url(self, object, kind, shop=None):
        return derive_model_url(AvailabilityException, "E-Commerce_admin:discounts_availability_exception", object, kind)
