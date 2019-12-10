# -*- coding: utf-8 -*-
# This file is part of E-Commerce.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.

from django.utils.translation import ugettext_lazy as _

from E-Commerce.xtheme import Theme


class E-CommerceTestingTheme(Theme):
    identifier = "E-Commerce_testing"
    name = _("E-Commerce Testing Theme")
    author = "E-Commerce Team"
    template_dir = "E-Commerce_testing"

    plugins = [__name__ + ".plugins.HighlightTestPlugin"]


class E-CommerceTestingThemeWithCustomBase(E-CommerceTestingTheme):
    identifier = "E-Commerce_testing_with_custom_base_template"
    name = _("E-Commerce Testing Theme With Custom Base Template")
    default_template_dir = "default_templates"
