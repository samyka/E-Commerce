# -*- coding: utf-8 -*-
# This file is part of E-Commerce.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from E-Commerce.testing import factories
from E-Commerce.xtheme.editing import could_edit, is_edit_mode, set_edit_mode
from E-Commerce_tests.utils.faux_users import SuperUser


def test_edit_priv(rf):
    request = rf.get("/")
    request.user = SuperUser()
    request.shop = factories.get_default_shop()
    request.session = {}
    assert could_edit(request)
    assert not is_edit_mode(request)
    set_edit_mode(request, True)
    assert is_edit_mode(request)
    set_edit_mode(request, False)
    assert not is_edit_mode(request)
