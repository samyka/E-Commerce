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


class ImportAdminModule(AdminModule):
    name = _("Data Import")
    breadcrumbs_menu_entry = MenuEntry(name, url="E-Commerce_admin:importer.import")

    def get_urls(self):
        return [
            admin_url(
                "^importer/import$",
                "E-Commerce.importer.admin_module.import_views.ImportView",
                name="importer.import"
            ),
            admin_url(
                "^importer/import/process$",
                "E-Commerce.importer.admin_module.import_views.ImportProcessView",
                name="importer.import_process"
            ),
            admin_url(
                "^importer/example$",
                "E-Commerce.importer.admin_module.import_views.ExampleFileDownloadView",
                name="importer.download_example"
            ),
        ]

    def get_menu_entries(self, request):
        return [
            MenuEntry(
                text=_("Data Import"),
                category=SETTINGS_MENU_CATEGORY,
                url="E-Commerce_admin:importer.import",
                icon="fa fa-star"
            )
        ]
