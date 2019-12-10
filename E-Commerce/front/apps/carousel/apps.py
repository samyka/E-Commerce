# -*- coding: utf-8 -*-
# This file is part of E-Commerce.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
import E-Commerce.apps


class AppConfig(E-Commerce.apps.AppConfig):
    name = "E-Commerce.front.apps.carousel"
    label = "carousel"
    provides = {
        "admin_module": [
            "E-Commerce.front.apps.carousel.admin_module:CarouselModule"
        ],
        "xtheme_plugin": [
            "E-Commerce.front.apps.carousel.plugins:CarouselPlugin",
            "E-Commerce.front.apps.carousel.plugins:BannerBoxPlugin"
        ],
    }
