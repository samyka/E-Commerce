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
from E-Commerce.admin.utils.urls import (
    admin_url, derive_model_url, get_edit_and_list_urls
)
from E-Commerce.core.models import ServiceProvider


class ServiceProviderModule(AdminModule):
    name = _("Service Providers")
    category = _("Payment and Shipping")

    def get_urls(self):
        return [
            admin_url(
                "^service_provider/(?P<pk>\d+)/delete/$",
                "E-Commerce.admin.modules.service_providers.views.ServiceProviderDeleteView",
                name="service_provider.delete"
            )
        ] + get_edit_and_list_urls(
            url_prefix="^service_provider",
            view_template="E-Commerce.admin.modules.service_providers.views.ServiceProvider%sView",
            name_template="service_provider.%s"
        )

    def get_menu_category_icons(self):
        return {self.category: "fa fa-cubes"}

    def get_menu_entries(self, request):
        return [
            MenuEntry(
                text=self.name,
                icon="fa fa-truck",
                url="E-Commerce_admin:service_provider.list",
                category=STOREFRONT_MENU_CATEGORY,
                ordering=3
            )
        ]

    def get_model_url(self, object, kind, shop=None):
        return derive_model_url(ServiceProvider, "E-Commerce_admin:service_provider", object, kind)
