# This file is part of E-Commerce.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _

import E-Commerce.apps


class AppConfig(E-Commerce.apps.AppConfig):
    name = "E-Commerce.order_printouts"
    verbose_name = _("Order printouts")
    label = "E-Commerce_order_printouts"

    provides = {
        "admin_module": [
            "E-Commerce.order_printouts.admin_module:PrintoutsAdminModule"
        ],
        "admin_order_section": [
            "E-Commerce.order_printouts.admin_module.section:PrintoutsSection"
        ],
    }
