# This file is part of E-Commerce.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from django.conf import settings

from E-Commerce.apps.provides import get_provide_objects


class BaseSettingsProvider(object):
    provided_settings = []

    def offers(self, setting_key):
        return bool(setting_key in self.provided_settings)

    def get_setting_value(self, setting_key):
        return None


class E-CommerceSettings(object):
    @classmethod
    def get_setting(cls, setting_key):
        for provider_cls in get_provide_objects("E-Commerce_settings_provider"):
            provider = provider_cls()
            if provider.offers(setting_key):
                return provider.get_setting_value(setting_key)
        return getattr(settings, setting_key)
