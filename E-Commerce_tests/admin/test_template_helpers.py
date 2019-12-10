# -*- coding: utf-8 -*-
# This file is part of E-Commerce.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
import mock
from django.core.urlresolvers import reverse

from E-Commerce.admin.template_helpers.E-Commerce_admin import get_config
from E-Commerce.testing.utils import apply_request_middleware
from E-Commerce.admin.browser_config import DefaultBrowserConfigProvider


def test_get_config(rf, admin_user):
    request = apply_request_middleware(rf.get("/"), user=admin_user)
    context = dict(request=request)
    config = get_config(context)
    for key, url in DefaultBrowserConfigProvider.get_browser_urls(request).items():
        assert config["browserUrls"][key] == reverse(url)
    assert "minSearchInputLength" in DefaultBrowserConfigProvider.get_gettings(request).keys()
