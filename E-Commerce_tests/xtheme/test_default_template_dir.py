# -*- coding: utf-8 -*-
# This file is part of E-Commerce.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
import pytest
from django.core.urlresolvers import reverse
from django.test import override_settings

from E-Commerce.core import cache
from E-Commerce.testing.factories import get_default_shop
from E-Commerce.testing.themes import (
    E-CommerceTestingTheme, E-CommerceTestingThemeWithCustomBase
)
from E-Commerce.xtheme.testing import override_current_theme_class
from E-Commerce_tests.utils import SmartClient


@pytest.mark.django_db
def test_theme_without_default_template_dir():
    with override_settings(CACHES={
        'default': {
            'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
            'LOCATION': 'test_configuration_cache',
        }
    }):
        cache.init_cache()

        with override_current_theme_class(E-CommerceTestingTheme, get_default_shop()):
            c = SmartClient()
            soup = c.soup(reverse("E-Commerce:index"))
            assert "Simple base for themes to use" not in soup
            assert "Welcome to test E-Commerce!" in soup.find("div", {"class": "page-content"}).text


@pytest.mark.django_db
def test_theme_with_default_template_dir():
    with override_settings(CACHES={
        'default': {
            'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
            'LOCATION': 'test_configuration_cache',
        }
    }):
        cache.init_cache()
        get_default_shop()
        with override_current_theme_class(E-CommerceTestingThemeWithCustomBase, get_default_shop()):
            c = SmartClient()
            soup = c.soup(reverse("E-Commerce:index"))
            assert "Simple base for themes to use" in soup.find("h1").text
            assert "Welcome to test E-Commerce!" in soup.find("h1").text
