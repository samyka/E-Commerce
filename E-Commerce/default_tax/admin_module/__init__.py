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
from E-Commerce.admin.utils.urls import derive_model_url, get_edit_and_list_urls
from E-Commerce.default_tax.models import TaxRule


class TaxRulesAdminModule(AdminModule):
    name = _("Tax Rules")
    breadcrumbs_menu_entry = MenuEntry(name, "E-Commerce_admin:default_tax.tax_rule.list")

    def get_urls(self):
        return get_edit_and_list_urls(
            url_prefix="^default-tax/rules",
            view_template="E-Commerce.default_tax.admin_module.views.TaxRule%sView",
            name_template="default_tax.tax_rule.%s"
        )

    def get_menu_entries(self, request):
        return [
            MenuEntry(
                text=_("Tax Rules"),
                icon="fa fa-file-text",
                url="E-Commerce_admin:default_tax.tax_rule.list",
                category=SETTINGS_MENU_CATEGORY,
                ordering=4,
                aliases=[_("Show tax rules")]
            )
        ]

    def get_model_url(self, object, kind, shop=None):
        return derive_model_url(TaxRule, "E-Commerce_admin:default_tax.tax_rule", object, kind)
