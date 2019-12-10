# -*- coding: utf-8 -*-
# This file is part of E-Commerce.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
import six
from django.contrib.auth import get_user_model
from django.db.models import Q
from django.utils.translation import ugettext_lazy as _

from E-Commerce.admin.base import AdminModule, MenuEntry, SearchResult
from E-Commerce.admin.menu import SETTINGS_MENU_CATEGORY
from E-Commerce.admin.utils.urls import admin_url, derive_model_url, get_model_url
from E-Commerce.admin.views.home import HelpBlockCategory, SimpleHelpBlock


class UserModule(AdminModule):
    name = _("Users")
    breadcrumbs_menu_entry = MenuEntry(name, url="E-Commerce_admin:user.list")

    def get_urls(self):
        return [
            admin_url(
                "^users/(?P<pk>\d+)/change-password/$",
                "E-Commerce.admin.modules.users.views.UserChangePasswordView",
                name="user.change-password"
            ),
            admin_url(
                "^users/(?P<pk>\d+)/reset-password/$",
                "E-Commerce.admin.modules.users.views.UserResetPasswordView",
                name="user.reset-password"
            ),
            admin_url(
                "^users/(?P<pk>\d+)/change-permissions/$",
                "E-Commerce.admin.modules.users.views.UserChangePermissionsView",
                name="user.change-permissions"
            ),
            admin_url(
                "^users/(?P<pk>\d+)/$",
                "E-Commerce.admin.modules.users.views.UserDetailView",
                name="user.detail"
            ),
            admin_url(
                "^users/new/$",
                "E-Commerce.admin.modules.users.views.UserDetailView",
                kwargs={"pk": None},
                name="user.new"
            ),
            admin_url(
                "^users/$",
                "E-Commerce.admin.modules.users.views.UserListView",
                name="user.list"
            ),
            admin_url(
                "^users/(?P<pk>\d+)/login/$",
                "E-Commerce.admin.modules.users.views.LoginAsUserView",
                name="user.login-as"
            ),
            admin_url(
                "^contacts/list-settings/",
                "E-Commerce.admin.modules.settings.views.ListSettingsView",
                name="user.list_settings"
            )
        ]

    def get_menu_entries(self, request):
        return [
            MenuEntry(
                text=_("Users"),
                icon="fa fa-users",
                url="E-Commerce_admin:user.list",
                category=SETTINGS_MENU_CATEGORY,
                ordering=1
            )
        ]

    def get_search_results(self, request, query):
        minimum_query_length = 3
        if len(query) >= minimum_query_length:
            users = get_user_model().objects.filter(
                Q(username__icontains=query) |
                Q(email=query)
            )
            for i, user in enumerate(users[:10]):
                relevance = 100 - i
                yield SearchResult(
                    text=six.text_type(user),
                    url=get_model_url(user),
                    category=_("Contacts"),
                    relevance=relevance
                )

    def get_help_blocks(self, request, kind):
        yield SimpleHelpBlock(
            text=_("Add some users to help manage your shop"),
            actions=[{
                "text": _("New user"),
                "url": self.get_model_url(get_user_model(), "new")
            }],
            priority=3,
            category=HelpBlockCategory.CONTACTS,
            icon_url="E-Commerce_admin/img/users.png",
            done=request.shop.staff_members.exclude(id=request.user.id).exists() if kind == "setup" else False,
            required=False
        )

    def get_model_url(self, object, kind, shop=None):
        return derive_model_url(get_user_model(), "E-Commerce_admin:user", object, kind)
