# This file is part of E-Commerce.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from E-Commerce.apps import AppConfig


class AuthAppConfig(AppConfig):
    name = "E-Commerce.front.apps.auth"
    verbose_name = "E-Commerce Frontend - User Authentication"
    label = "E-Commerce_front.auth"

    provides = {
        "front_urls": [
            "E-Commerce.front.apps.auth.urls:urlpatterns"
        ],
    }


default_app_config = "E-Commerce.front.apps.auth.AuthAppConfig"
