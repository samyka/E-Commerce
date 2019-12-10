# -*- coding: utf-8 -*-
# This file is part of E-Commerce.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from django.utils.translation import ugettext_lazy as _

from E-Commerce.admin.base import AdminModule, MenuEntry
from E-Commerce.admin.menu import CONTENT_MENU_CATEGORY
from E-Commerce.admin.utils.urls import admin_url


class MediaModule(AdminModule):
    """
    A module for handling site media.
    Basically a frontend for the Django-Filer app.
    """

    name = _("Media")

    def get_urls(self):
        return [
            admin_url(
                "^media/$",
                "E-Commerce.admin.modules.media.views.MediaBrowserView",
                name="media.browse"
            ),
            admin_url(
                "^media/upload/$",
                "E-Commerce.admin.modules.media.views.media_upload",
                name="media.upload"
            )
        ]

    def get_menu_entries(self, request):
        return [
            MenuEntry(
                text=_("Media browser"),
                icon="fa fa-folder-open",
                url="E-Commerce_admin:media.browse",
                category=CONTENT_MENU_CATEGORY,
                ordering=2
            ),
        ]
