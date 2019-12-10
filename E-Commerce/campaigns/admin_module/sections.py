# -*- coding: utf-8 -*-
# This file is part of E-Commerce.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from django.utils.translation import ugettext_lazy as _

from E-Commerce.admin.base import Section
from E-Commerce.admin.shop_provider import get_shop
from E-Commerce.admin.supplier_provider import get_supplier
from E-Commerce.campaigns.models import BasketCampaign
from E-Commerce.core.models import ShopProduct


class ProductCampaignsSection(Section):
    identifier = "product_campaigns"
    name = _("Active Basket Campaigns")
    icon = "fa-bullhorn"
    template = "E-Commerce/campaigns/admin/_product_campaigns.jinja"

    @classmethod
    def visible_for_object(cls, product, request=None):
        return bool(product.pk)

    @classmethod
    def get_context_data(cls, product, request=None):
        ctx = {}
        shop = get_shop(request)
        try:
            shop_product = product.get_shop_instance(shop)
            basket_campaigns = BasketCampaign.get_for_product(shop_product)
            supplier = get_supplier(request)
            if supplier:
                basket_campaigns = basket_campaigns.filter(supplier=supplier)

            ctx[shop] = {"basket_campaigns": basket_campaigns}
            return ctx
        except ShopProduct.DoesNotExist:
            return ctx
