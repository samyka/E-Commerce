# This file is part of E-Commerce.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
"""
E-Commerce Registration Add-on
=========================

The E-Commerce.front.apps.registration add-on provides simple user
registration and email token based activation.

It is based on the django-registration-redux package.

Installation
------------

Add ``registration`` and ``E-Commerce.front.apps.registration``
into your ``INSTALLED_APPS`` (and run migrations, of course).

The application registers its URLs via the ``front_urls`` provides
mechanism.

URL names
---------

* ``E-Commerce:registration_register`` -- the entry point for registration.
"""

import django.conf
from registration.signals import user_activated

from E-Commerce.apps import AppConfig
from E-Commerce.front.apps.registration.signals import company_contact_activated


class RegistrationAppConfig(AppConfig):
    name = "E-Commerce.front.apps.registration"
    verbose_name = "E-Commerce Frontend - User Registration"
    label = "E-Commerce_front.registration"

    required_installed_apps = {
        "registration": "django-registration-redux is required for user registration and activation"
    }

    provides = {
        "front_urls": [
            "E-Commerce.front.apps.registration.urls:urlpatterns"
        ],
        "notify_event": [
            "E-Commerce.front.apps.registration.notify_events:RegistrationReceived",
            "E-Commerce.front.apps.registration.notify_events:CompanyRegistrationReceived",
            "E-Commerce.front.apps.registration.notify_events:CompanyApproved"
        ],
        "notify_script_template": [
            "E-Commerce.front.apps.registration.notify_events:RegistrationReceivedEmailScriptTemplate",
            "E-Commerce.front.apps.registration.notify_events:CompanyRegistrationReceivedEmailScriptTemplate",
            "E-Commerce.front.apps.registration.notify_events:CompanyActivatedEmailScriptTemplate",
        ]
    }

    def ready(self):
        from E-Commerce.core.models import CompanyContact
        from .notify_events import send_company_activated_first_time_notification
        from .signals import handle_user_activation

        user_activated.connect(handle_user_activation)

        if not hasattr(django.conf.settings, "ACCOUNT_ACTIVATION_DAYS"):
            # Patch settings to include ACCOUNT_ACTIVATION_DAYS;
            # it's a setting owned by `django-registration-redux`,
            # but not set to a default value. If it's not set, a crash
            # will occur when attempting to create an account, so
            # for convenience, we're doing what `django-registration-redux`
            # didn't wanna.
            django.conf.settings.ACCOUNT_ACTIVATION_DAYS = 7

        if not hasattr(django.conf.settings, "REGISTRATION_AUTO_LOGIN"):
            # By default, Django-Registration considers this False, but
            # we override it to True. unless otherwise set by the user.
            django.conf.settings.REGISTRATION_AUTO_LOGIN = True

        if not hasattr(django.conf.settings, "REGISTRATION_EMAIL_HTML"):
            # We only provide txt templates out of the box, so default to
            # false for HTML mails.
            django.conf.settings.REGISTRATION_EMAIL_HTML = False

        company_contact_activated.connect(
            send_company_activated_first_time_notification,
            sender=CompanyContact,
        )


default_app_config = "E-Commerce.front.apps.registration.RegistrationAppConfig"
