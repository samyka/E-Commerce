# -*- coding: utf-8 -*-
# This file is part of E-Commerce.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from __future__ import unicode_literals

from E-Commerce.utils import update_module_attributes

from ._process import CheckoutProcess, VerticalCheckoutProcess
from ._services import (
    BasicServiceCheckoutPhaseProvider, ServiceCheckoutPhaseProvider
)
from ._view_mixin import CheckoutPhaseViewMixin

__all__ = [
    "BasicServiceCheckoutPhaseProvider",
    "CheckoutPhaseViewMixin",
    "CheckoutProcess",
    "ServiceCheckoutPhaseProvider",
    "VerticalCheckoutProcess",
]

update_module_attributes(__all__, __name__)
