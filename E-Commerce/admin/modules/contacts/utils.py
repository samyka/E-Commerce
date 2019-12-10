# -*- coding: utf-8 -*-
# This file is part of E-Commerce.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from django.conf import settings
from django.core.exceptions import PermissionDenied

from E-Commerce.admin.shop_provider import get_shop


def request_limited(request):
    return (settings.E-Commerce_ENABLE_MULTIPLE_SHOPS and settings.E-Commerce_MANAGE_CONTACTS_PER_SHOP and
            not request.user.is_superuser)


def check_contact_permission(request, contact):
    shop = get_shop(request)
    if request_limited(request) and not contact.in_shop(shop):
        raise PermissionDenied()
