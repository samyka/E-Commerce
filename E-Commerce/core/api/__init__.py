# -*- coding: utf-8 -*-
# This file is part of E-Commerce.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from E-Commerce.core.api.address import MutableAddressViewSet
from E-Commerce.core.api.attribute import AttributeViewSet
from E-Commerce.core.api.basket import BasketViewSet
from E-Commerce.core.api.category import CategoryViewSet
from E-Commerce.core.api.contacts import ContactViewSet, PersonContactViewSet
from E-Commerce.core.api.contact_group import ContactGroupViewSet
from E-Commerce.core.api.contact_group_price_display import (
    ContactGroupPriceDisplayViewSet
)
from E-Commerce.core.api.front_orders import FrontOrderViewSet
from E-Commerce.core.api.front_passwords import (
    PasswordResetViewSet, SetPasswordViewSet
)
from E-Commerce.core.api.front_products import (
    FrontProductViewSet, FrontShopProductViewSet
)
from E-Commerce.core.api.front_users import FrontUserViewSet
from E-Commerce.core.api.manufacturer import ManufacturerViewSet
from E-Commerce.core.api.orders import OrderViewSet
from E-Commerce.core.api.product_media import ProductMediaViewSet
from E-Commerce.core.api.product_variation import (
    ProductVariationVariableValueViewSet, ProductVariationVariableViewSet
)
from E-Commerce.core.api.products import (
    ProductAttributeViewSet, ProductPackageViewSet, ProductTypeViewSet,
    ProductViewSet, ShopProductViewSet
)
from E-Commerce.core.api.shipments import ShipmentViewSet
from E-Commerce.core.api.shop import ShopViewSet
from E-Commerce.core.api.suppliers import SupplierViewSet
from E-Commerce.core.api.tax import TaxViewSet
from E-Commerce.core.api.tax_class import TaxClassViewSet
from E-Commerce.core.api.units import SalesUnitViewSet
from E-Commerce.core.api.users import UserViewSet


def populate_core_api(router):
    """
    :param router: Router
    :type router: rest_framework.routers.DefaultRouter
    """
    router.register("E-Commerce/address", MutableAddressViewSet)
    router.register("E-Commerce/attribute", AttributeViewSet)
    router.register("E-Commerce/category", CategoryViewSet)
    router.register("E-Commerce/contact", ContactViewSet)
    router.register("E-Commerce/contact_group", ContactGroupViewSet)
    router.register("E-Commerce/contact_group_price_display", ContactGroupPriceDisplayViewSet)
    router.register("E-Commerce/order", OrderViewSet)
    router.register("E-Commerce/person_contact", PersonContactViewSet)
    router.register("E-Commerce/product", ProductViewSet)
    router.register("E-Commerce/product_attribute", ProductAttributeViewSet)
    router.register("E-Commerce/product_media", ProductMediaViewSet)
    router.register("E-Commerce/product_type", ProductTypeViewSet)
    router.register("E-Commerce/product_package", ProductPackageViewSet)
    router.register("E-Commerce/product_variation_variable", ProductVariationVariableViewSet)
    router.register("E-Commerce/product_variation_variable_value", ProductVariationVariableValueViewSet)
    router.register("E-Commerce/shipment", ShipmentViewSet)
    router.register("E-Commerce/shop", ShopViewSet)
    router.register("E-Commerce/shop_product", ShopProductViewSet)
    router.register("E-Commerce/manufacturer", ManufacturerViewSet)
    router.register("E-Commerce/supplier", SupplierViewSet)
    router.register("E-Commerce/user", UserViewSet)
    router.register("E-Commerce/sales_unit", SalesUnitViewSet)
    router.register("E-Commerce/tax", TaxViewSet)
    router.register("E-Commerce/tax_class", TaxClassViewSet)
    router.register("E-Commerce/basket", BasketViewSet)

    router.register("E-Commerce/front/user", FrontUserViewSet)
    router.register("E-Commerce/front/password", SetPasswordViewSet, 'set_password')
    router.register("E-Commerce/front/password/reset", PasswordResetViewSet, 'password_reset')
    router.register("E-Commerce/front/orders", FrontOrderViewSet)
    router.register("E-Commerce/front/shop_products", FrontShopProductViewSet)
    router.register("E-Commerce/front/products", FrontProductViewSet)
