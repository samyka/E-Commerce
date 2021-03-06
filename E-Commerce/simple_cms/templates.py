# -*- coding: utf-8 -*-
# This file is part of E-Commerce.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from django.utils.translation import ugettext as _


class SimpleCMSDefaultTemplate(object):
    name = _("Default Page")
    template_path = "E-Commerce/simple_cms/page.jinja"


class SimpleCMSTemplateSidebar(object):
    name = _("Page with sidebar")
    template_path = "E-Commerce/simple_cms/page_sidebar.jinja"
