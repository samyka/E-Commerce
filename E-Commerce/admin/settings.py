# -*- coding: utf-8 -*-
# This file is part of E-Commerce.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from __future__ import unicode_literals

"""
Settings of E-Commerce Admin.

See :ref:`apps-settings` (in :obj:`E-Commerce.apps`) for general information
about the E-Commerce settings system.  Especially, when inventing settings of
your own, the :ref:`apps-naming-settings` section is an important read.
"""

#: Spec which defines a list of Wizard Panes to be shown in E-Commerce Admin
#: for E-Commerce initialization and configuration.
#:
#: Panes must be subclasses of `E-Commerce.admin.views.WizardPane`.
#:
E-Commerce_SETUP_WIZARD_PANE_SPEC = []

#: Spec which defines a function that loads and return discovered admin modules.
#: This function should return a list of `E-Commerce.admin.base.AdminModule`
#:
E-Commerce_GET_ADMIN_MODULES_SPEC = ("E-Commerce.admin.module_registry.get_admin_modules")

#: Spec which defines the Shop provider.
#: The shop provider is the interface responsible for fetching and setting
#: the active shop in admin module
#:
E-Commerce_ADMIN_SHOP_PROVIDER_SPEC = ("E-Commerce.admin.shop_provider.AdminShopProvider")
#: URL address to E-Commerce Merchant Documentation and Guide.
#: The URL must end with a slash.
#:
E-Commerce_ADMIN_MERCHANT_DOCS_PAGE = "https://E-Commerce-guide.readthedocs.io/en/latest/"

#: The minimum number of characters required to start a search
#:
E-Commerce_ADMIN_MINIMUM_INPUT_LENGTH_SEARCH = 3

#: Spec that defines the Supplier Provider for a given request
#:
E-Commerce_ADMIN_SUPPLIER_PROVIDER_SPEC = (
    "E-Commerce.admin.supplier_provider.DefaultSupplierProvider")

#: The input format to be used in date pickers
#:
E-Commerce_ADMIN_DATE_INPUT_FORMAT = "Y-m-d"

#: The input format to be used in datetime pickers
#:
E-Commerce_ADMIN_DATETIME_INPUT_FORMAT = "Y-m-d H:i"

#: The input format to be used in time pickers
#:
E-Commerce_ADMIN_TIME_INPUT_FORMAT = "H:i"


#: The input step to be used for time pickers
#:
E-Commerce_ADMIN_DATETIME_INPUT_STEP = 15

#: Menu category identifiers that should always activate the
#: menu item. Useful in case there is need to always open some
#: certain menus.
E-Commerce_ALWAYS_ACTIVE_MENU_CATEGORY_IDENTIFIERS = []
