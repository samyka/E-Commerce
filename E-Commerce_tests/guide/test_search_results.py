# -*- coding: utf-8 -*-
# This file is part of E-Commerce.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
import pytest
from django.conf import settings
from django.test.utils import override_settings

from E-Commerce.admin.module_registry import replace_modules
from E-Commerce.admin.views.search import get_search_results
from E-Commerce.guide.admin_module import GuideAdminModule


@pytest.mark.django_db
def test_search(client, rf):
    if "E-Commerce.guide" not in settings.INSTALLED_APPS:
        pytest.skip("Need E-Commerce.guide in INSTALLED_APPS")
    request = rf.get("/")
    search_term = "customer"
    request.session = client.session
    with replace_modules([GuideAdminModule]):
        with override_settings(E-Commerce_GUIDE_FETCH_RESULTS=False):
            results = get_search_results(request, search_term)
            assert [r for r in results if search_term in r.text]
