# -*- coding: utf-8 -*-
# This file is part of E-Commerce.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from django.db import models

from E-Commerce.core.fields import MoneyValueField
from E-Commerce.utils.properties import MoneyPropped, PriceProperty


class SupplierPrice(MoneyPropped, models.Model):
    shop = models.ForeignKey("E-Commerce.Shop")
    supplier = models.ForeignKey("E-Commerce.Supplier")
    product = models.ForeignKey("E-Commerce.Product")
    amount_value = MoneyValueField()
    amount = PriceProperty("amount_value", "shop.currency", "shop.prices_include_tax")
