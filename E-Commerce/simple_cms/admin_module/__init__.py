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
from E-Commerce.admin.menu import CONTENT_MENU_CATEGORY
from E-Commerce.admin.utils.urls import derive_model_url, get_edit_and_list_urls, admin_url
from E-Commerce.admin.views.home import HelpBlockCategory, SimpleHelpBlock
from E-Commerce.simple_cms.models import Page


class SimpleCMSAdminModule(AdminModule):
    name = _(u"Content Pages")
    breadcrumbs_menu_entry = MenuEntry(name, "E-Commerce_admin:simple_cms.page.list")

    def get_urls(self):
        url_prefix = "^cms/page"
        view_template = "E-Commerce.simple_cms.admin_module.views.Page%sView"
        name_template = "simple_cms.page.%s"
        return get_edit_and_list_urls(
            url_prefix=url_prefix,
            view_template=view_template,
            name_template=name_template,
        ) + [admin_url(
            r"%s/delete/(?P<pk>\d+)/" % url_prefix,
            view_template % "Delete",
            name=name_template % "delete",
            permissions=(name_template % "delete",)
        ), ]

    def get_menu_entries(self, request):
        return [
            MenuEntry(
                text=_("Pages"), icon="fa fa-file-text",
                url="E-Commerce_admin:simple_cms.page.list",
                category=CONTENT_MENU_CATEGORY,
                ordering=3,
                aliases=[_("Show pages")]
            )
        ]

    def get_help_blocks(self, request, kind):
        if kind == "quicklink":
            yield SimpleHelpBlock(
                text=_("Add a web page"),
                actions=[{
                    "text": _("New page"),
                    "url": self.get_model_url(Page, "new")
                }],
                priority=100,
                category=HelpBlockCategory.STOREFRONT,
                icon_url="simple_cms/page.png"
            )

    def get_model_url(self, object, kind, shop=None):
        return derive_model_url(Page, "E-Commerce_admin:simple_cms.page", object, kind)
