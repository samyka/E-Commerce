# -*- coding: utf-8 -*-
# This file is part of E-Commerce.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.

from django.contrib import messages
from django.shortcuts import redirect
from django.utils.translation import ugettext_lazy as _
from django.views.generic import FormView

from E-Commerce.api.admin_module.forms import APIPermissionForm


class APIPermissionView(FormView):
    template_name = "E-Commerce/api/admin/permissions.jinja"
    form_class = APIPermissionForm

    def form_valid(self, form):
        form.save()
        messages.success(self.request, _("API permissions saved"))
        return redirect("E-Commerce_admin:api_permission")
