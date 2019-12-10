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
from E-Commerce.admin.menu import REPORTS_MENU_CATEGORY
from E-Commerce.admin.utils.urls import admin_url
from E-Commerce.reports.report import get_report_classes


class ReportsAdminModule(AdminModule):
    name = _("Reports")
    breadcrumbs_menu_entry = MenuEntry(text=name, url="E-Commerce_admin:reports.list")

    def get_urls(self):
        return [
            admin_url(
                "^reports/$",
                "E-Commerce.reports.admin_module.views.ReportView",
                name="reports.list"
            )
        ]

    def get_menu_entries(self, request):
        return [
            MenuEntry(
                text=self.name,
                icon="fa fa-image",
                url="E-Commerce_admin:reports.list",
                category=REPORTS_MENU_CATEGORY
            )
        ]

    def get_extra_permissions(self):
        report_identifiers = set()
        for report_class in get_report_classes():
            report_identifiers.add(report_class)
        return report_identifiers
