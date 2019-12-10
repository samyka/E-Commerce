# -*- coding: utf-8 -*-
# This file is part of E-Commerce.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.

from django.core.urlresolvers import reverse_lazy
from django.views.generic import DeleteView

from E-Commerce.core.models import ContactGroup


class ContactGroupDeleteView(DeleteView):
    model = ContactGroup
    success_url = reverse_lazy("E-Commerce_admin:contact_group.list")
