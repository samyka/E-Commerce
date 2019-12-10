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
    name = __name__
    verbose_name = _('E-Commerce Frontend - Recently Viewed Products')
    label = 'E-Commerce_front.recently_viewed_products'

    provides = {
        "xtheme_plugin": [
            __name__ + ".plugins:RecentlyViewedProductsPlugin",
        ],
        "xtheme_resource_injection": [__name__ + ".plugins:add_resources"],
    }


default_app_config = __name__ + '.AppConfig'
