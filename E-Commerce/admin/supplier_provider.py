# -*- coding: utf-8 -*-
# This file is part of E-Commerce.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from E-Commerce.utils.importing import cached_load


class DefaultSupplierProvider(object):
    @classmethod
    def get_supplier(cls, request, **kwargs):
        return None


def get_supplier(request, **kwargs):
    return cached_load("E-Commerce_ADMIN_SUPPLIER_PROVIDER_SPEC").get_supplier(request, **kwargs)
