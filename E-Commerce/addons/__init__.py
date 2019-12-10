# This file is part of E-Commerce.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from E-Commerce.apps import AppConfig

from .manager import add_enabled_addons

__all__ = ["add_enabled_addons"]


class E-CommerceAddonsAppConfig(AppConfig):
    name = "E-Commerce.addons"
    verbose_name = "E-Commerce Addons"
    label = "E-Commerce_addons"

    provides = {
        "admin_module": [
            "E-Commerce.addons.admin_module:AddonModule",
        ]
    }


default_app_config = "E-Commerce.addons.E-CommerceAddonsAppConfig"
