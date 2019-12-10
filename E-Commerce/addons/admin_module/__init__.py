# -*- coding: utf-8 -*-
# This file is part of E-Commerce.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from django.utils.translation import ugettext_lazy as _

from E-Commerce.admin.base import AdminModule, MenuEntry
from E-Commerce.admin.menu import ADDONS_MENU_CATEGORY
from E-Commerce.admin.utils.urls import admin_url


class AddonModule(AdminModule):
    name = _("Addons")
    breadcrumbs_menu_entry = MenuEntry(text=name, url="E-Commerce_admin:addon.list")

    def get_urls(self):
        return [
            admin_url(
                "^addons/$",
                "E-Commerce.addons.admin_module.views.AddonListView",
                name="addon.list"
            ),
            admin_url(
                "^addons/add/$",
                "E-Commerce.addons.admin_module.views.AddonUploadView",
                name="addon.upload"
            ),
            admin_url(
                "^addons/add/confirm/$",
                "E-Commerce.addons.admin_module.views.AddonUploadConfirmView",
                name="addon.upload_confirm"
            ),
            admin_url(
                "^addons/reload/$",
                "E-Commerce.addons.admin_module.views.ReloadView",
                name="addon.reload"
            ),
        ]

    def get_menu_entries(self, request):
        return [
            MenuEntry(
                text=_("Addons"),
                icon="fa fa-puzzle-piece",
                url="E-Commerce_admin:addon.list",
                category=ADDONS_MENU_CATEGORY
            )
        ]
