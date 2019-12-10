# -*- coding: utf-8 -*-
# This file is part of E-Commerce.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
import django.conf

from E-Commerce.apps import AppConfig
from E-Commerce.core.excs import MissingSettingException
from E-Commerce.utils import money


class E-CommerceCoreAppConfig(AppConfig):
    name = "E-Commerce.core"
    verbose_name = "E-Commerce Core"
    label = "E-Commerce"  # Use "E-Commerce" as app_label instead of "core"
    required_installed_apps = (
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "easy_thumbnails",
        "filer",
    )
    provides = {
        "api_populator": [
            "E-Commerce.core.api:populate_core_api"
        ],
        "pricing_module": [
            "E-Commerce.core.pricing.default_pricing:DefaultPricingModule"
        ],
        "order_source_validator": [
            "E-Commerce.core.order_creator:OrderSourceMinTotalValidator",
            "E-Commerce.core.order_creator:OrderSourceMethodsUnavailabilityReasonsValidator",
            "E-Commerce.core.order_creator:OrderSourceSupplierValidator",
        ]
    }

    def ready(self):
        from django.conf import settings
        if not getattr(settings, "PARLER_DEFAULT_LANGUAGE_CODE", None):
            raise MissingSettingException("PARLER_DEFAULT_LANGUAGE_CODE must be set.")
        if not getattr(settings, "PARLER_LANGUAGES", None):
            raise MissingSettingException("PARLER_LANGUAGES must be set.")

        # set money precision provider function
        from .models import get_currency_precision
        money.set_precision_provider(get_currency_precision)

        if django.conf.settings.E-Commerce_ERROR_PAGE_HANDLERS_SPEC:
            from .error_handling import install_error_handlers
            install_error_handlers()

        # connect signals
        import E-Commerce.core.signal_handers    # noqa: F401


default_app_config = "E-Commerce.core.E-CommerceCoreAppConfig"
