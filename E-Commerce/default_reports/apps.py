# This file is part of E-Commerce.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
import E-Commerce.apps


class AppConfig(E-Commerce.apps.AppConfig):
    name = "E-Commerce.default_reports"
    provides = {
        "reports": [
            "E-Commerce.default_reports.reports.sales:SalesReport",
            "E-Commerce.default_reports.reports.total_sales:TotalSales",
            "E-Commerce.default_reports.reports.sales_per_hour:SalesPerHour",
            "E-Commerce.default_reports.reports.product_total_sales:ProductSalesReport",
            "E-Commerce.default_reports.reports.new_customers:NewCustomersReport",
            "E-Commerce.default_reports.reports.customer_sales:CustomerSalesReport",
            "E-Commerce.default_reports.reports.taxes:TaxesReport",
            "E-Commerce.default_reports.reports.shipping:ShippingReport",
            "E-Commerce.default_reports.reports.refunds.RefundedSalesReport",
        ],
    }
