# -*- coding: utf-8 -*-
# This file is part of E-Commerce.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from E-Commerce.apps import AppConfig


def activate_sqlite_fk_constraint(sender, connection, **kwargs):
    """Enable integrity constraint with SQLite and not running browser tests."""
    import os
    if connection.vendor == 'sqlite' and os.environ.get("E-Commerce_BROWSER_TESTS") != "1":
        cursor = connection.cursor()
        cursor.execute('PRAGMA foreign_keys = ON;')


class E-CommerceTestingAppConfig(AppConfig):
    name = "E-Commerce.testing"
    verbose_name = "E-Commerce Testing & Demo Utilities"
    label = "E-Commerce_testing"
    provides = {
        "admin_module": [
            "E-Commerce.testing.modules.mocker:TestingAdminModule",
            "E-Commerce.testing.modules.sample_data:SampleDataAdminModule",
            "E-Commerce.testing.modules.demo:DemoModule",
        ],
        "service_provider_admin_form": [
            "E-Commerce.testing.service_forms:PseudoPaymentProcessorForm",
            "E-Commerce.testing.service_forms:PaymentWithCheckoutPhaseForm",
            "E-Commerce.testing.service_forms:CarrierWithCheckoutPhaseForm",
        ],
        "front_service_checkout_phase_provider": [
            "E-Commerce.testing.simple_checkout_phase.PaymentPhaseProvider",
            "E-Commerce.testing.simple_checkout_phase.ShipmentPhaseProvider",
        ],
        "admin_contact_toolbar_button": [
            "E-Commerce.testing.modules.mocker.toolbar:MockContactToolbarButton",
        ],
        "admin_contact_toolbar_action_item": [
             "E-Commerce.testing.modules.mocker.toolbar:MockContactToolbarActionItem",
        ],
        "admin_contact_edit_toolbar_button": [
            "E-Commerce.testing.modules.mocker.toolbar:MockContactToolbarButton",
        ],
        "admin_product_toolbar_action_item": [
            "E-Commerce.testing.modules.mocker.toolbar:MockProductToolbarActionItem",
        ],
        "admin_contact_section": [
            "E-Commerce.testing.modules.mocker.sections:MockContactSection",
        ],
        "importers": [
            "E-Commerce.testing.importers.DummyImporter",
            "E-Commerce.testing.importers.DummyFileImporter"
        ],
        "xtheme": [
            __name__ + ".themes:E-CommerceTestingTheme",
            __name__ + ".themes:E-CommerceTestingThemeWithCustomBase",
        ],
        "pricing_module": [
            "E-Commerce.testing.supplier_pricing.pricing:SupplierPricingModule"
        ],
    }

    def ready(self):
        from django.db.backends.signals import connection_created
        connection_created.connect(activate_sqlite_fk_constraint)


default_app_config = "E-Commerce.testing.E-CommerceTestingAppConfig"
