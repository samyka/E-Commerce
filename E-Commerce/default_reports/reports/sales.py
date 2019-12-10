# -*- coding: utf-8 -*-
# This file is part of E-Commerce.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
import itertools

from babel.dates import format_date
from django.utils.timezone import localtime
from django.utils.translation import ugettext_lazy as _

from E-Commerce.core.pricing import TaxfulPrice, TaxlessPrice
from E-Commerce.default_reports.forms import OrderReportForm
from E-Commerce.default_reports.mixins import OrderReportMixin
from E-Commerce.reports.report import E-CommerceReportBase
from E-Commerce.utils.i18n import get_current_babel_locale


class SalesReport(OrderReportMixin, E-CommerceReportBase):
    identifier = "sales_report"
    title = _("Sales Report")
    form_class = OrderReportForm

    filename_template = "sales-report-%(time)s"
    schema = [
        {"key": "date", "title": _("Date")},
        {"key": "order_count", "title": _("Orders")},
        {"key": "product_count", "title": _("Products")},
        {"key": "taxless_total", "title": _("Taxless Total")},
        {"key": "taxful_total", "title": _("Taxful Total")},
    ]

    def extract_date(self, entity):
        return localtime(entity.order_date).date()

    def get_data(self):
        orders = self.get_objects().order_by("-order_date")
        data = []
        # TODO: maybe make raw sql query in future
        for order_date, orders_group in itertools.groupby(orders, key=self.extract_date):
            taxless_total = TaxlessPrice(0, currency=self.shop.currency)
            taxful_total = TaxfulPrice(0, currency=self.shop.currency)
            product_count = 0
            order_count = 0
            for order in orders_group:
                taxless_total += order.taxless_total_price
                taxful_total += order.taxful_total_price
                product_count += sum(order.get_product_ids_and_quantities().values())
                order_count += 1

            data.append({
                "date": format_date(order_date, locale=get_current_babel_locale()),
                "order_count": order_count,
                "product_count": int(product_count),
                "taxless_total": taxless_total.as_rounded().value,
                "taxful_total": taxful_total.as_rounded().value,
            })

        return self.get_return_data(data)
