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
from E-Commerce.admin.menu import STOREFRONT_MENU_CATEGORY
from E-Commerce.admin.utils.urls import derive_model_url, get_edit_and_list_urls
from E-Commerce.core.models import Manufacturer


class ManufacturerModule(AdminModule):
    name = _("Manufacturers")
    breadcrumbs_menu_entry = MenuEntry(name, url="E-Commerce_admin:manufacturer.list")

    def get_urls(self):
        return get_edit_and_list_urls(
            url_prefix="^manufacturers",
            view_template="E-Commerce.admin.modules.manufacturers.views.Manufacturer%sView",
            name_template="manufacturer.%s"
        )

    def get_menu_entries(self, request):
        return [
            MenuEntry(
                text=_("Manufacturers"),
                icon="fa fa-building",
                url="E-Commerce_admin:manufacturer.list",
                category=STOREFRONT_MENU_CATEGORY,
                ordering=4
            ),
        ]

    def get_model_url(self, object, kind, shop=None):
        return derive_model_url(Manufacturer, "E-Commerce_admin:manufacturer", object, kind)
