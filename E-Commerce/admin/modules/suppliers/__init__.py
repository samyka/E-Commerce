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
from E-Commerce.admin.utils.urls import derive_model_url, get_edit_and_list_urls, admin_url
from E-Commerce.core.models import Supplier


class SupplierModule(AdminModule):
    name = _("Suppliers")
    breadcrumbs_menu_entry = MenuEntry(name, url="E-Commerce_admin:supplier.list")

    def get_urls(self):
        return get_edit_and_list_urls(
            url_prefix="^suppliers",
            view_template="E-Commerce.admin.modules.suppliers.views.Supplier%sView",
            name_template="supplier.%s"
        ) + [admin_url(
            "^suppliers/delete/(?P<pk>\d+)/$",
            "E-Commerce.admin.modules.suppliers.views.SupplierDeleteView",
            name="supplier.delete",
            permissions=("supplier.delete",)
        ), ]

    def get_menu_entries(self, request):
        return [
            MenuEntry(
                text=_("Suppliers"),
                icon="fa fa-truck",
                url="E-Commerce_admin:supplier.list",
                category=STOREFRONT_MENU_CATEGORY,
                ordering=7
            ),
        ]

    def get_model_url(self, object, kind, shop=None):
        return derive_model_url(Supplier, "E-Commerce_admin:supplier", object, kind)
