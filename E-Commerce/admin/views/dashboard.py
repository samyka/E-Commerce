# -*- coding: utf-8 -*-
# This file is part of E-Commerce.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect
from django.views.generic.base import TemplateView

import E-Commerce
from E-Commerce.admin.dashboard import get_activity
from E-Commerce.admin.dashboard.blocks import DashboardBlock
from E-Commerce.admin.module_registry import get_modules
from E-Commerce.admin.shop_provider import get_shop
from E-Commerce.admin.utils.permissions import get_missing_permissions
from E-Commerce.admin.utils.tour import is_tour_complete
from E-Commerce.admin.utils.wizard import setup_wizard_complete
from E-Commerce.core.telemetry import try_send_telemetry


class DashboardView(TemplateView):
    template_name = "E-Commerce/admin/dashboard/dashboard.jinja"

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        context["version"] = E-Commerce.__version__
        context["notifications"] = notifications = []
        context["blocks"] = blocks = []
        for module in get_modules():
            if not get_missing_permissions(self.request.user, module.get_required_permissions()):
                notifications.extend(module.get_notifications(request=self.request))
                blocks.extend(module.get_dashboard_blocks(request=self.request))

        # sort blocks by sort order and size, trying to make them fit better
        blocks.sort(key=lambda block: (block.sort_order, DashboardBlock.SIZES.index(block.size)))
        context["activity"] = get_activity(request=self.request)
        context["tour_key"] = "dashboard"
        context["tour_complete"] = is_tour_complete(get_shop(self.request), "dashboard", user=self.request.user)
        return context

    def get(self, request, *args, **kwargs):
        try_send_telemetry(request)
        if not setup_wizard_complete(request):
            return HttpResponseRedirect(reverse("E-Commerce_admin:wizard"))
        elif request.shop.maintenance_mode:
            return HttpResponseRedirect(reverse("E-Commerce_admin:home"))
        return super(DashboardView, self).get(request, *args, **kwargs)
