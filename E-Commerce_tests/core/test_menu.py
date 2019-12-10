# -*- coding: utf-8 -*-
# This file is part of E-Commerce.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from __future__ import unicode_literals

import pytest

from E-Commerce.admin.base import BaseMenuEntry
from E-Commerce.admin.menu import MAIN_MENU, extend_main_menu
from E-Commerce.apps.provides import override_provides


def test_menu_updater():
    main_menu = extend_main_menu(MAIN_MENU)
    assert len(list(filter(lambda x: 'entries' in x,  main_menu))) == 0

    with override_provides("admin_main_menu_updater",
                           ["E-Commerce.testing.admin_main_menu_updater:TestAdminMainMenuUpdater"]):
        main_menu = extend_main_menu(MAIN_MENU)
        assert len(list(filter(lambda x: 'entries' in x,  main_menu))) == 1


def test_base_menu_entry():
    entry = BaseMenuEntry()

    # test Resolver
    assert entry.url is None

    admin_url = ('E-Commerce_admin:dashboard', (), {})
    entry._url = admin_url
    assert entry.url == '/sa/'
    assert entry.original_url == admin_url

    entry._url = 'E-Commerce_admin:dashboard'
    assert entry.url == '/sa/'

    entry._url = '/sa/'
    assert entry.url == '/sa/'

    with pytest.raises(TypeError):
        entry._url = 1
        assert not entry.url

    # test iterator
    assert entry.has_entries is False
    entry.entries = [BaseMenuEntry(), BaseMenuEntry(),]
    assert entry.has_entries is True
    assert len(list(e for e in entry)) == 2
