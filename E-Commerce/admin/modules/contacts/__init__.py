# -*- coding: utf-8 -*-
# This file is part of E-Commerce.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
import six
from django.conf import settings
from django.db.models import Q
from django.utils.translation import ugettext_lazy as _

from E-Commerce.admin.base import AdminModule, MenuEntry, SearchResult
from E-Commerce.admin.menu import CONTACTS_MENU_CATEGORY
from E-Commerce.admin.utils.urls import admin_url, derive_model_url, get_model_url
from E-Commerce.core.models import Contact


class ContactModule(AdminModule):
    name = _("Contacts")
    breadcrumbs_menu_entry = MenuEntry(text=name, url="E-Commerce_admin:contact.list", category=CONTACTS_MENU_CATEGORY)

    def get_urls(self):
        return [
            admin_url(
                "^contacts/new/$",
                "E-Commerce.admin.modules.contacts.views.ContactEditView",
                kwargs={"pk": None},
                name="contact.new"
            ),
            admin_url(
                "^contacts/(?P<pk>\d+)/edit/$",
                "E-Commerce.admin.modules.contacts.views.ContactEditView",
                name="contact.edit"
            ),
            admin_url(
                "^contacts/(?P<pk>\d+)/$",
                "E-Commerce.admin.modules.contacts.views.ContactDetailView",
                name="contact.detail"
            ),
            admin_url(
                "^contacts/reset-password/(?P<pk>\d+)/$",
                "E-Commerce.admin.modules.contacts.views.ContactResetPasswordView",
                name="contact.reset_password"
            ),
            admin_url(
                "^contacts/$",
                "E-Commerce.admin.modules.contacts.views.ContactListView",
                name="contact.list"
            ),
            admin_url(
                "^contacts/list-settings/",
                "E-Commerce.admin.modules.settings.views.ListSettingsView",
                name="contact.list_settings"
            ),
            admin_url(
                "^contacts/mass-edit/$",
                "E-Commerce.admin.modules.contacts.views.ContactMassEditView",
                name="contact.mass_edit"
            ),
            admin_url(
                "^contacts/mass-edit-group/$",
                "E-Commerce.admin.modules.contacts.views.ContactGroupMassEditView",
                name="contact.mass_edit_group"
            )
        ]

    def get_menu_entries(self, request):
        return [
            MenuEntry(
                text=_("Contacts"), icon="fa fa-users",
                url="E-Commerce_admin:contact.list",
                category=CONTACTS_MENU_CATEGORY,
                ordering=1
            )
        ]

    def get_search_results(self, request, query):
        minimum_query_length = 3
        if len(query) >= minimum_query_length:
            filters = Q(Q(name__icontains=query) | Q(email=query))

            # show only contacts which the shop has access
            if settings.E-Commerce_ENABLE_MULTIPLE_SHOPS and settings.E-Commerce_MANAGE_CONTACTS_PER_SHOP:
                filters &= Q(shops=request.shop)

            if not request.user.is_superuser:
                filters &= ~Q(PersonContact___user__is_superuser=True)

            contacts = Contact.objects.filter(filters)
            for i, contact in enumerate(contacts[:10]):
                relevance = 100 - i
                yield SearchResult(
                    text=six.text_type(contact), url=get_model_url(contact),
                    category=_("Contacts"), relevance=relevance
                )

    def get_model_url(self, object, kind, shop=None):
        return derive_model_url(Contact, "E-Commerce_admin:contact", object, kind)
