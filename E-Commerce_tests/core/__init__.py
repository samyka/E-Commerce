# -*- coding: utf-8 -*-
# This file is part of E-Commerce.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from E-Commerce.apps import AppConfig


class AppConfig(AppConfig):
    name = 'E-Commerce_tests.core'
    label = 'E-Commerce_tests_core'

    provides = {
        "module_test_module": [
            "E-Commerce_tests.core.module_test_module:ModuleTestModule",
            "E-Commerce_tests.core.module_test_module:AnotherModuleTestModule",
        ]
    }


default_app_config = 'E-Commerce_tests.core.AppConfig'
