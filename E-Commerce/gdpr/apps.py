# This file is part of E-Commerce.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
import E-Commerce.apps


class AppConfig(E-Commerce.apps.AppConfig):
    name = "E-Commerce.gdpr"
    label = "E-Commerce_gdpr"
    provides = {
        "admin_module": [
            "E-Commerce.gdpr.admin_module.GDPRModule"
        ],
        "front_urls": [
            "E-Commerce.gdpr.urls:urlpatterns"
        ],
        "customer_dashboard_items": [
            "E-Commerce.gdpr.dashboard_items:GDPRDashboardItem"
        ],
        "admin_contact_toolbar_action_item": [
            "E-Commerce.gdpr.admin_module.toolbar:AnonymizeContactToolbarButton",
            "E-Commerce.gdpr.admin_module.toolbar:DownloadDataToolbarButton",
        ],
        "xtheme_resource_injection": [
            "E-Commerce.gdpr.resources:add_gdpr_consent_resources"
        ],
        "front_registration_field_provider": [
            "E-Commerce.gdpr.providers:GDPRRegistrationFieldProvider"
        ],
        "front_auth_form_field_provider": [
            "E-Commerce.gdpr.providers:GDPRAuthFieldProvider"
        ],
        "checkout_confirm_form_field_provider": [
            "E-Commerce.gdpr.providers:GDPRCheckoutFieldProvider"
        ],
        "front_company_registration_form_provider": [
            "E-Commerce.gdpr.providers:GDPRFormDefProvider"
        ]
    }

    def ready(self):
        # connect receivers
        import E-Commerce.gdpr.receivers  # noqa: F401
