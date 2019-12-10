# -*- coding: utf-8 -*-
# This file is part of E-Commerce.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from __future__ import unicode_literals

from E-Commerce.apps import AppConfig


class SimpleSearchAppConfig(AppConfig):
    name = "E-Commerce.front.apps.simple_search"
    verbose_name = "E-Commerce Frontend - Simple Search"
    label = "E-Commerce_front.simple_search"

    provides = {
        "front_urls": [
            "E-Commerce.front.apps.simple_search.urls:urlpatterns"
        ],
        "front_extend_product_list_form": [
            "E-Commerce.front.apps.simple_search.forms.FilterProductListByQuery",
        ],
        "front_template_helper_namespace": [
            "E-Commerce.front.apps.simple_search.template_helpers:TemplateHelpers"
        ]
    }


default_app_config = "E-Commerce.front.apps.simple_search.SimpleSearchAppConfig"
