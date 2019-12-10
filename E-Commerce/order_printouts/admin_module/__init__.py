# -*- coding: utf-8 -*-
# This file is part of E-Commerce.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from __future__ import unicode_literals

from E-Commerce.admin.base import AdminModule
from E-Commerce.admin.utils.urls import admin_url


class PrintoutsAdminModule(AdminModule):
    def get_urls(self):
        return [
            admin_url(
                "^printouts/delivery/(?P<shipment_pk>\d+)/$",
                "E-Commerce.order_printouts.admin_module.views.get_delivery_pdf",
                name="printouts.delivery_pdf"
            ),
            admin_url(
                "^printouts/delivery/html/(?P<shipment_pk>\d+)/$",
                "E-Commerce.order_printouts.admin_module.views.get_delivery_html",
                name="printouts.delivery_html"
            ),
            admin_url(
                "^printouts/delivery/email/(?P<shipment_pk>\d+)/$",
                "E-Commerce.order_printouts.admin_module.views.send_delivery_email",
                name="printouts.delivery_email"
            ),
            admin_url(
                "^printouts/confirmation/(?P<order_pk>\d+)/$",
                "E-Commerce.order_printouts.admin_module.views.get_confirmation_pdf",
                name="printouts.confirmation_pdf"
            ),
            admin_url(
                "^printouts/confirmation/html/(?P<order_pk>\d+)/$",
                "E-Commerce.order_printouts.admin_module.views.get_confirmation_html",
                name="printouts.confirmation_html"
            ),
            admin_url(
                "^printouts/confirmation/email/(?P<order_pk>\d+)/$",
                "E-Commerce.order_printouts.admin_module.views.send_confirmation_email",
                name="printouts.confirmation_email"
            ),
        ]