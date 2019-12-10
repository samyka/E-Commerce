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
from E-Commerce.admin.utils.urls import derive_model_url, get_edit_and_list_urls
from E-Commerce.core.models import Attribute


class AttributeModule(AdminModule):
    name = _("Attributes")
    breadcrumbs_menu_entry = MenuEntry(text=name, url="E-Commerce_admin:attribute.list")

    def get_urls(self):
        return get_edit_and_list_urls(
            url_prefix="^attributes",
            view_template="E-Commerce.admin.modules.attributes.views.Attribute%sView",
            name_template="attribute.%s"
        )

    def get_menu_category_icons(self):
        return {self.name: "fa fa-tags"}

    def get_menu_entries(self, request):
        return [
            MenuEntry(
                text=_("Attributes"),
                icon="fa fa-tags",
                url="E-Commerce_admin:attribute.list",
                category=STOREFRONT_MENU_CATEGORY,
                ordering=8
            )
        ]

    def get_model_url(self, object, kind, shop=None):
        return derive_model_url(Attribute, "E-Commerce_admin:attribute", object, kind)
