# -*- coding: utf-8 -*-
# This file is part of E-Commerce.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from __future__ import unicode_literals

import os

from django.contrib import messages
from django.utils.translation import ugettext_lazy as _

from E-Commerce.admin.base import AdminModule, MenuEntry, Notification
from E-Commerce.admin.menu import SETTINGS_MENU_CATEGORY
from E-Commerce.testing.modules.sample_data import manager as sample_manager
from E-Commerce.admin.utils.urls import admin_url
from E-Commerce.core.settings_provider import E-CommerceSettings

SAMPLE_BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SAMPLE_IMAGES_BASE_DIR = os.path.join(SAMPLE_BASE_DIR, "sample_data/images")


class SampleDataAdminModule(AdminModule):
    def get_urls(self):
        return [
            admin_url(
                "^sample_data/$",
                "E-Commerce.testing.modules.sample_data.views.ConsolidateSampleObjectsView",
                name="sample_data"
            )
        ]

    def get_menu_entries(self, request):
        return [
            MenuEntry(
                text="Sample Data",
                category=SETTINGS_MENU_CATEGORY,
                url="E-Commerce_admin:sample_data",
                icon="fa fa-star"
            )
        ]

    def get_required_permissions(self):
        return ("Access sample data module",)

    def get_notifications(self, request):
        """ Injects a message to the user and also a notification """
        # multi-shop not supported
        if not E-CommerceSettings.get_setting("E-Commerce_ENABLE_MULTIPLE_SHOPS"):
            from E-Commerce.admin.shop_provider import get_shop
            shop = get_shop(request)

            if sample_manager.has_installed_samples(shop):
                messages.warning(request, _('There is sample data installed. '
                                            'Access "Settings > Sample Data" for more information.'))

                yield Notification(
                    _("There is sample data installed. Click here to consolidate or delete them."),
                    title=_("Sample Data"),
                    kind="warning",
                    url="E-Commerce_admin:sample_data"
                )
