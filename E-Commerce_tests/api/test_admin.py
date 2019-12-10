# -*- coding: utf-8 -*-
# This file is part of E-Commerce.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
import pytest

from E-Commerce import configuration
from E-Commerce.api.admin_module.views.permissions import APIPermissionView
from E-Commerce.api.permissions import make_permission_config_key, PermissionLevel
from E-Commerce.core import cache
from E-Commerce.core.api.users import UserViewSet
from E-Commerce.testing.factories import get_default_shop
from E-Commerce.testing.utils import apply_request_middleware


def setup_function(fn):
    cache.clear()


@pytest.mark.django_db
def test_consolidate_objects(rf):
    get_default_shop()

    # just visit to make sure GET is ok
    request = apply_request_middleware(rf.get("/"))
    response = APIPermissionView.as_view()(request)
    assert response.status_code == 200

    perm_key = make_permission_config_key(UserViewSet())
    assert configuration.get(None, perm_key) is None

    # now post the form to see what happens
    request = apply_request_middleware(rf.post("/", {perm_key: PermissionLevel.ADMIN}))
    response = APIPermissionView.as_view()(request)
    assert response.status_code == 302      # good
    assert int(configuration.get(None, perm_key)) == PermissionLevel.ADMIN
