# -*- coding: utf-8 -*-
# This file is part of E-Commerce.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from __future__ import unicode_literals

from E-Commerce.admin.base import AdminModule, MenuEntry
from E-Commerce.admin.menu import SETTINGS_MENU_CATEGORY
from E-Commerce.admin.utils.urls import admin_url


class TestingAdminModule(AdminModule):
    def get_urls(self):
        return [
            admin_url(
                "^mocker/$",
                "E-Commerce.testing.modules.mocker.mocker_view.MockerView",
                name="mocker"
            )
        ]

    def get_menu_entries(self, request):
        return [
            MenuEntry(
                text="Create Mock Objects",
                category=SETTINGS_MENU_CATEGORY,
                url="E-Commerce_admin:mocker",
                icon="fa fa-star"
            )
        ]
