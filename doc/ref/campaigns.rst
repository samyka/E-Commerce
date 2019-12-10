Discounts in E-Commerce
==================

E-Commerce provides two ways to give discounts for products.
First way `DiscountModule <E-Commerce.core.pricing.DiscountModule>` and
second being the `OrderSourceModifierModule <E-Commerce.core.pricing.OrderSourceModifierModule>`.
Both of these function very differently and are explained in this document.

Unlike the `PricingModule <E-Commerce.core.pricing.PricingModule>`, there can be multiple
modules which provide discounts to the product at any given time.

DiscountModule
--------------

This module can give discounts based on the given context for a given product.
There is one implementation using the `DiscountModule <E-Commerce.core.pricing.DiscountModule>`
currently in E-Commerce: `CatalogCampaignModule <E-Commerce.campaigns.modules.CatalogCampaignModule>`.


OrderSourceModifierModule
-------------------------

This module directly modifies the given `OrderSource <E-Commerce.core.order_creator.OrderSource>`.

There is currently one implementation using the
`OrderSourceModifierModule <E-Commerce.core.pricing.OrderSourceModifierModule>`
E-Commerce: `BasketCampaignModule <E-Commerce.campaigns.modules.BasketCampaignModule>`.


Campaigns
---------

The E-Commerce base installation comes with :ref:`catalog-campaigns`
and :ref:`basket-campaigns` which are polymorphic models.

To determine if a campaign should be applied, E-Commerce looks for
the filters and conditions for the campaign. If a matching campaign is
found, an effect will be applied.

.. _catalog-campaigns:

Catalog Campaign
----------------

A `CatalogCampaignModule <E-Commerce.campaigns.models.CatalogCampaign>` directly applies
discounts to products when browsing the catalog. If a catalog campaign matches,
it usually matches everywhere in the shop, basket and catalog.

To determine if a catalog campaign matches, E-Commerce looks for filters and conditions

Catalog Filters
^^^^^^^^^^^^^^^

`CatalogFilter <E-Commerce.campaigns.models.CatalogFilter>` can filter product querysets
and matches directly to product properties.


Context Conditions
^^^^^^^^^^^^^^^^^^

`ContextCondition <E-Commerce.campaigns.models.ContextCondition>` matches
based on context. This is handy if you need to give a discount for
a certain customer group or something that is available in context.


Product Discount Effects
^^^^^^^^^^^^^^^^^^^^^^^^

`ProductDiscountEffect <E-Commerce.campaigns.models.ProductDiscountEffect>` gives the
discount for product. This modifiers the products ``PriceInfo`` directly by
setting the ``price``.

.. _basket-campaigns:

Basket Campaign
---------------

A campaign that affects only the products in basket. E-Commerce checks basket
conditions to see if a basket campaign should be applied. Basket campaigns
can also require a coupon to activate.

Basket Conditions
^^^^^^^^^^^^^^^^^

`BasketCondition <E-Commerce.campaigns.models.BasketCondition>` matches the
basket contents to activate. For example, basket campaigns can use basket
conditions to check the number of products in the customer basket to
determine if the campaign should apply.

Basket Discount Effects
^^^^^^^^^^^^^^^^^^^^^^^

`BasketDiscountEffect <E-Commerce.campaigns.models.BasketDiscountEffect>` matches
the basket contents to activate. This effect returns a discount amount
value that can be used to create a new line for example.

Basket Line Effects
^^^^^^^^^^^^^^^^^^^

`BasketLineEffect <E-Commerce.campaigns.models.BasketLineEffect>` matches
the basket contents to activate. This effect adds a new line to the order
source which can be used to give a free product
