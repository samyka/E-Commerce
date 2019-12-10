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
from E-Commerce.admin.menu import SETTINGS_MENU_CATEGORY
from E-Commerce.admin.utils.urls import admin_url


class AdminMenuModule(AdminModule):
    """
    Module that customizes dashboard admin menu
    """
    name = _("Admin menu")
    breadcrumbs_menu_entry = MenuEntry(name, url="E-Commerce_admin:menu.arrange")

    def get_urls(self):
        return [
            admin_url(
                r"^menu/$",
                "E-Commerce.admin.modules.menu.views.AdminMenuArrangeView",
                name="menu.arrange"
            ),
            admin_url(
                r"^menu/reset/$",
                "E-Commerce.admin.modules.menu.views.AdminMenuResetView",
                name="menu.reset"
            ),
        ]

    def get_menu_entries(self, request):
        category = SETTINGS_MENU_CATEGORY
        return [
            MenuEntry(
                text=_("Admin menu"),
                icon="fa fa-list-alt",
                url="E-Commerce_admin:menu.arrange",
                category=category,
                ordering=1
            ),
        ]
