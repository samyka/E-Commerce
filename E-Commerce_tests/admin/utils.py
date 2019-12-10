# -*- coding: utf-8 -*-
# This file is part of E-Commerce.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from E-Commerce_tests.utils import replace_urls


def get_admin_only_urls():
    from django.conf.urls import url, include
    from E-Commerce.admin.urls import get_urls
    class FauxUrlPatternsModule:
        urlpatterns = get_urls()

    return [
        url(r'^sa/', include(FauxUrlPatternsModule, namespace="E-Commerce_admin", app_name="E-Commerce_admin")),
    ]

def admin_only_urls():
    return replace_urls(get_admin_only_urls())
