# This file is part of E-Commerce.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from django.db import models

from E-Commerce.core.models import ShopProduct


class CatalogFilterCachedShopProduct(models.Model):
    filter = models.ForeignKey('CatalogFilter', related_name='cached_shop_products', db_index=True)
    shop_product = models.ForeignKey(ShopProduct, related_name='cached_catalog_campaign_filters', db_index=True)
