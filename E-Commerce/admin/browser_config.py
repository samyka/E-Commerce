# -*- coding: utf-8 -*-
# This file is part of E-Commerce.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from django.conf import settings

from E-Commerce.admin.utils.permissions import has_permission
from E-Commerce.utils.i18n import get_current_babel_locale


class BaseBrowserConfigProvider(object):
    @classmethod
    def get_browser_urls(cls, request, **kwargs):
        return {}

    @classmethod
    def get_gettings(cls, request, **kwargs):
        return {}


class DefaultBrowserConfigProvider(BaseBrowserConfigProvider):
    @classmethod
    def get_browser_urls(cls, request, **kwargs):
        return {
            "edit": "E-Commerce_admin:edit",
            "select": "E-Commerce_admin:select",
            "media": ("E-Commerce_admin:media.browse" if has_permission(request.user, "E-Commerce_admin:media.browse") else None),
            "product": "E-Commerce_admin:shop_product.list",
            "contact": "E-Commerce_admin:contact.list",
            "setLanguage": "E-Commerce_admin:set-language",
            "tour": "E-Commerce_admin:tour",
            "menu_toggle": "E-Commerce_admin:menu_toggle"
        }

    @classmethod
    def get_gettings(cls, request, **kwargs):
        return {
            "minSearchInputLength": settings.E-Commerce_ADMIN_MINIMUM_INPUT_LENGTH_SEARCH or 1,
            "dateInputFormat": settings.E-Commerce_ADMIN_DATE_INPUT_FORMAT,
            "datetimeInputFormat": settings.E-Commerce_ADMIN_DATETIME_INPUT_FORMAT,
            "timeInputFormat": settings.E-Commerce_ADMIN_TIME_INPUT_FORMAT,
            "datetimeInputStep": settings.E-Commerce_ADMIN_DATETIME_INPUT_STEP,
            "dateInputLocale": get_current_babel_locale().language,
            "staticPrefix": settings.STATIC_URL,
        }
