# This file is part of E-Commerce.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
import E-Commerce.apps


class AppConfig(E-Commerce.apps.AppConfig):
    name = "E-Commerce.tasks"
    label = "E-Commerce_tasks"
    provides = {
        "admin_module": [
            "E-Commerce.tasks.admin_module.TaskAdminModule",
            "E-Commerce.tasks.admin_module.TaskTypeAdminModule"
        ]
    }
