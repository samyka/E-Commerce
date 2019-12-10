# -*- coding: utf-8 -*-
# This file is part of E-Commerce.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from __future__ import unicode_literals

from django.core.urlresolvers import reverse_lazy

from E-Commerce.admin.modules.contact_group_price_display.views.forms import \
    ContactGroupPriceDisplayForm
from E-Commerce.admin.utils.views import CreateOrUpdateView
from E-Commerce.core.models import ContactGroupPriceDisplay


class ContactGroupPriceDisplayEditView(CreateOrUpdateView):
    model = ContactGroupPriceDisplay
    form_class = ContactGroupPriceDisplayForm
    template_name = "E-Commerce/admin/contact_group_price_display/edit.jinja"
    context_object_name = "price_display"
    add_form_errors_as_messages = True

    def get_form_kwargs(self):
        kwargs = super(ContactGroupPriceDisplayEditView, self).get_form_kwargs()
        kwargs["request"] = self.request
        return kwargs

    def get_success_url(self):
        return reverse_lazy("E-Commerce_admin:contact_group_price_display.list")
