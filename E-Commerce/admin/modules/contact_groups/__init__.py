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
from E-Commerce.admin.menu import CONTACTS_MENU_CATEGORY
from E-Commerce.admin.utils.urls import (
    admin_url, derive_model_url, get_edit_and_list_urls
)
from E-Commerce.core.models import ContactGroup


class ContactGroupModule(AdminModule):
    name = _("Contact Groups")
    breadcrumbs_menu_entry = MenuEntry(name, url="E-Commerce_admin:contact_group.list")

    def get_urls(self):
        return [
            admin_url(
                "^contact_group/(?P<pk>\d+)/delete/$",
                "E-Commerce.admin.modules.contact_groups.views.ContactGroupDeleteView",
                name="contact_group.delete"
            )
        ] + get_edit_and_list_urls(
            url_prefix="^contact_group",
            view_template="E-Commerce.admin.modules.contact_groups.views.ContactGroup%sView",
            name_template="contact_group.%s"
        )

    def get_menu_entries(self, request):
        return [
            MenuEntry(
                text=self.name,
                icon="fa fa-asterisk",
                url="E-Commerce_admin:contact_group.list",
                category=CONTACTS_MENU_CATEGORY,
                ordering=2
            ),
        ]

    def get_model_url(self, object, kind, shop=None):
        return derive_model_url(ContactGroup, "E-Commerce_admin:contact_group", object, kind)
