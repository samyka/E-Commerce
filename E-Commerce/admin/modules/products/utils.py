# -*- coding: utf-8 -*-
# This file is part of E-Commerce.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from E-Commerce.core.models import ProductPackageLink


def clear_existing_package(parent_product):
    """
    Utility function for clearing existing package.
    """
    children = parent_product.get_package_child_to_quantity_map().keys()
    ProductPackageLink.objects.filter(parent=parent_product).delete()
    parent_product.verify_mode()
    parent_product.save()
    for child in children:
        child.verify_mode()
        child.save()
