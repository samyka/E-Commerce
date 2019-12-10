# -*- coding: utf-8 -*-
# This file is part of E-Commerce.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from E-Commerce.apps import AppConfig


class CampaignAppConfig(AppConfig):
    name = "E-Commerce.campaigns"
    verbose_name = "E-Commerce Campaigns"
    label = "campaigns"
    provides = {
        "admin_contact_group_form_part": [
            "E-Commerce.campaigns.admin_module.form_parts:SalesRangesFormPart"
        ],
        "discount_module": [
            "E-Commerce.campaigns.modules:CatalogCampaignModule"
        ],
        "order_source_modifier_module": [
            "E-Commerce.campaigns.modules:BasketCampaignModule"
        ],
        "admin_module": [
            "E-Commerce.campaigns.admin_module:CampaignAdminModule",
        ],
        "admin_product_section": [
            "E-Commerce.campaigns.admin_module.sections:ProductCampaignsSection"
        ],
        "campaign_basket_condition": [
            "E-Commerce.campaigns.admin_module.forms:BasketTotalProductAmountConditionForm",
            "E-Commerce.campaigns.admin_module.forms:BasketTotalAmountConditionForm",
            "E-Commerce.campaigns.admin_module.forms:BasketTotalUndiscountedProductAmountConditionForm",
            "E-Commerce.campaigns.admin_module.forms:BasketMaxTotalProductAmountConditionForm",
            "E-Commerce.campaigns.admin_module.forms:BasketMaxTotalAmountConditionForm",
            "E-Commerce.campaigns.admin_module.forms:ProductsInBasketConditionForm",
            "E-Commerce.campaigns.admin_module.forms:ContactGroupBasketConditionForm",
            "E-Commerce.campaigns.admin_module.forms:ContactBasketConditionForm",
            "E-Commerce.campaigns.admin_module.forms:CategoryProductsBasketConditionForm",
            "E-Commerce.campaigns.admin_module.forms:HourBasketConditionForm",
        ],
        "campaign_basket_discount_effect_form": [
            "E-Commerce.campaigns.admin_module.forms:BasketDiscountAmountForm",
            "E-Commerce.campaigns.admin_module.forms:BasketDiscountPercentageForm",
            "E-Commerce.campaigns.admin_module.forms:DiscountPercentageFromUndiscountedForm",
        ],
        "campaign_basket_line_effect_form": [
            "E-Commerce.campaigns.admin_module.forms:FreeProductLineForm",
            "E-Commerce.campaigns.admin_module.forms:DiscountFromProductForm",
            "E-Commerce.campaigns.admin_module.forms:DiscountFromCategoryProductsForm",
        ],
        "campaign_context_condition": [
            "E-Commerce.campaigns.admin_module.forms:ContactGroupConditionForm",
            "E-Commerce.campaigns.admin_module.forms:ContactConditionForm",
            "E-Commerce.campaigns.admin_module.forms:HourConditionForm",
        ],
        "campaign_catalog_filter": [
            "E-Commerce.campaigns.admin_module.forms:ProductTypeFilterForm",
            "E-Commerce.campaigns.admin_module.forms:ProductFilterForm",
            "E-Commerce.campaigns.admin_module.forms:CategoryFilterForm"
        ],
        "campaign_product_discount_effect_form": [
            "E-Commerce.campaigns.admin_module.forms:ProductDiscountAmountForm",
            "E-Commerce.campaigns.admin_module.forms:ProductDiscountPercentageForm",
        ],
        "reports": [
            "E-Commerce.campaigns.reports:CouponsUsageReport"
        ]
    }

    def ready(self):
        from django.db.models.signals import m2m_changed, post_save
        from E-Commerce.campaigns.models import CategoryFilter, ProductFilter, ProductTypeFilter
        from E-Commerce.campaigns.models import ContactCondition, ContactGroupCondition
        from E-Commerce.campaigns.signal_handlers import (
            invalidate_context_condition_cache,
            update_customers_groups, update_filter_cache
        )
        from E-Commerce.core.models import ContactGroup, Payment, ShopProduct
        post_save.connect(
            update_customers_groups,
            sender=Payment,
            dispatch_uid="contact_group_sales:update_customers_groups"
        )

        # Invalidate context condition caches
        m2m_changed.connect(
            invalidate_context_condition_cache,
            sender=ContactGroup.members.through,
            dispatch_uid="campaigns:invalidate_caches_for_contact_group_m2m_change"
        )
        m2m_changed.connect(
            invalidate_context_condition_cache,
            sender=ContactCondition.contacts.through,
            dispatch_uid="campaigns:invalidate_caches_for_contacts_condition_m2m_change"
        )
        m2m_changed.connect(
            invalidate_context_condition_cache,
            sender=ContactGroupCondition.contact_groups.through,
            dispatch_uid="campaigns:invalidate_caches_for_contact_group_condition_m2m_change"
        )

        # Invalidate context filter caches
        m2m_changed.connect(
            update_filter_cache,
            sender=CategoryFilter.categories.through,
            dispatch_uid="campaigns:invalidate_caches_for_category_filter_m2m_change"
        )
        m2m_changed.connect(
            update_filter_cache,
            sender=ProductFilter.products.through,
            dispatch_uid="campaigns:invalidate_caches_for_product_filter_m2m_change"
        )
        m2m_changed.connect(
            update_filter_cache,
            sender=ProductTypeFilter.product_types.through,
            dispatch_uid="campaigns:invalidate_caches_for_product_type_filter_m2m_change"
        )
        post_save.connect(
            update_filter_cache,
            sender=ShopProduct,
            dispatch_uid="campaigns:invalidate_caches_for_shop_product_save"
        )
        m2m_changed.connect(
            update_filter_cache,
            sender=ShopProduct.categories.through,
            dispatch_uid="campaigns:invalidate_caches_for_shop_product_m2m_change"
        )
