Implementation of Prices and Taxes in E-Commerce
===========================================

This document describes deeper details about price and tax
implementation in E-Commerce from a developer's point of view.  To understand
the basics, please read :doc:`../ref/prices_and_taxes` first.

.. _price-tax-types:

Types Used for Prices and Taxes
-------------------------------

`~E-Commerce.utils.money.Money`

  Used to represent money amounts (that are not prices).  It is
  basically a `~decimal.Decimal` number with a currency.

`~E-Commerce.core.pricing.Price`

  Used to represent prices. `Price` is a `~E-Commerce.utils.money.Money` with
  an `includes_tax` property.  It has has two subclasses:
  `~E-Commerce.core.pricing.TaxfulPrice` and
  `~E-Commerce.core.pricing.TaxlessPrice`.

  There should usually be no need to create prices directly with these
  classes; see :ref:`creating-prices`.

`~E-Commerce.core.pricing.Priceful`

  An interface for accessing the price information of a product, order
  line, basket line, or whatever.  See :ref:`accessing-prices`.

`~E-Commerce.core.pricing.PriceInfo`

  A class for describing an item's price information.

`~E-Commerce.core.pricing.PricingModule`

  An interface for querying prices of products.

`~E-Commerce.core.pricing.PricingContext`

  A container for variables that affect pricing.  Pricing modules may
  subclass this.

`~E-Commerce.core.pricing.PricingContextable`

  An interface for objects that can be converted to a pricing context.
  Instances of `PricingContext` or `~django.http.HttpRequest` satisfy
  this interface.

`~E-Commerce.core.taxing.LineTax`

  An interface for describing a calculated tax of a line in order or
  basket.  Has a reference to the line and to the applied tax and the
  calculated amount of tax. One line could have several taxes applied,
  each is presented with a separate `LineTax`.

`~E-Commerce.core.taxing.SourceLineTax`

  A container for a calculated tax of a
  `~E-Commerce.core.order_creator.SourceLine` (or
  `~E-Commerce.front.basket.objects.BasketLine`).  Implements the `LineTax`
  interface.

`~E-Commerce.core.models.OrderLineTax`

  A Django model for persistently storing the calculated tax of an
  `~E-Commerce.core.models.OrderLine`.  Implements the `LineTax` interface.

`~E-Commerce.core.models.Tax`

  A Django model for a tax with name, code, and percentage rate or fixed
  amount.  Fixed amounts are not yet supported.

  .. TODO:: Fix this when fixed amounts are supported.

`~E-Commerce.core.taxing.TaxableItem`

  An interface for items that can be taxed.  Implemented by
  `~E-Commerce.core.models.Product`, `~E-Commerce.core.models.ShippingMethod`,
  `~E-Commerce.core.models.PaymentMethod` and
  `~E-Commerce.core.order_creator.SourceLine`.

`~E-Commerce.core.models.TaxClass`

  A Django model for a tax class.  Taxable items (e.g. products, methods
  or lines) are grouped to tax classes to make it possible to have
  different taxation rules for different groups of items.

`~E-Commerce.core.models.CustomerTaxGroup`

  A Django model for grouping customers to make it possible to have
  different taxation rules for different groups of customers.  E-Commerce
  assigns separate `CustomerTaxGroup`s for a
  `~E-Commerce.core.models.PersonContact` and a
  `~E-Commerce.core.models.CompanyContact` by default.

`~E-Commerce.core.taxing.TaxModule`

  An interface for calculating the taxes of an
  `~E-Commerce.core.order_creator.OrderSource` or any `TaxableItem`.  The
  E-Commerce Base distribution ships a concrete implementation of a
  `TaxModule` called `~E-Commerce.default_tax.module.DefaultTaxModule`.  It
  is a based on a table of tax rules (saved with
  `~E-Commerce.default_tax.models.TaxRule` model).  See
  :ref:`default-tax-module`.  Used `TaxModule` can be changed with
  `~E-Commerce.core.settings.E-Commerce_TAX_MODULE` setting.

`~E-Commerce.core.taxing.TaxedPrice`

  A type to represent the return value of tax calculation.  Contains a
  pair of prices, `TaxfulPrice` and `TaxlessPrice`, of which one is the
  original price before the calculation and the other is the calculated
  price. Also contains a list of the applied taxes.  `TaxedPrice` is the
  return type of `~E-Commerce.core.taxing.TaxModule.get_taxed_price_for`
  method in the `TaxModule` interface.

`~E-Commerce.core.taxing.TaxingContext`

  A container for variables that affect taxing, such as customer tax
  group, customer tax number, location (country, postal code, etc.).
  Used in the `TaxModule` interface. Note: This is *not* usually
  subclassed.

.. _creating-prices:

Creating Prices
---------------

When implementing a `~E-Commerce.core.pricing.PricingModule` or another
module that has to create prices, use the `Shop.create_price
<E-Commerce.core.models.Shop.create_price>` method.  It makes sure that all
prices have the same :ref:`price unit <price-unit>`.

.. _accessing-prices:

Accessing Prices of Product or Line
-----------------------------------

There is a `~E-Commerce.core.pricing.Priceful` interface for accessing
prices.  It is implemented by `~E-Commerce.core.models.OrderLine` and
`~E-Commerce.core.order_creator.SourceLine`,
`~E-Commerce.front.basket.objects.BasketLine`, and
`~E-Commerce.core.pricing.PriceInfo` which is returned e.g. by
`~E-Commerce.core.models.Product.get_price_info` method.
