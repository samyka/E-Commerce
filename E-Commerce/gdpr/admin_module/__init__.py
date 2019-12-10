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


class GDPRModule(AdminModule):
    name = _("GDPR")

    def get_urls(self):
        return [
            admin_url(
                "^gdpr/$",
                "E-Commerce.gdpr.admin_module.views.GDPRView",
                name="gdpr.settings"
            ),
            admin_url(
                "^gdpr/contact/(?P<pk>\d+)/anonymize/$",
                "E-Commerce.gdpr.admin_module.views.GDPRAnonymizeView",
                name="gdpr.anonymize"
            ),
            admin_url(
                "^gdpr/contact/(?P<pk>\d+)/download/$",
                "E-Commerce.gdpr.admin_module.views.GDPRDownloadDataView",
                name="gdpr.download_data"
            )
        ]

    def get_menu_entries(self, request):
        return [
            MenuEntry(
                text=_("GDPR"),
                icon="fa fa-shield",
                url="E-Commerce_admin:gdpr.settings",
                category=SETTINGS_MENU_CATEGORY,
            ),
        ]
