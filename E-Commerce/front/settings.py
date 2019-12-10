# This file is part of E-Commerce.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.


#: This is used to get the login form for the login dropdown in navigation.jinja
E-Commerce_LOGIN_VIEW = (
    "E-Commerce.front.apps.auth.views:LoginView")

#: Spec string for the class used for creating Order from a Basket.
#:
#: This is the easiest way to customize the order creation process
#: without having to override a single URL or touch the ``E-Commerce.front`` code.
E-Commerce_BASKET_ORDER_CREATOR_SPEC = (
    "E-Commerce.core.basket.order_creator:BasketOrderCreator")

#: Spec string for the Django CBV (or an API-compliant class) for the basket view.
#:
#: This view deals with ``/basket/``.
E-Commerce_BASKET_VIEW_SPEC = (
    "E-Commerce.front.views.basket:DefaultBasketView")

#: Spec string for the command dispatcher used when products are added/deleted/etc.
#: from the basket.
#:
#: This view deals with commands ``POST``ed to ``/basket/``.
E-Commerce_BASKET_COMMAND_DISPATCHER_SPEC = (
    "E-Commerce.core.basket.command_dispatcher:BasketCommandDispatcher")

#: Spec string for the update method dispatcher used when the basket is updated (usually
#: on the basket page).
E-Commerce_BASKET_UPDATE_METHODS_SPEC = (
    "E-Commerce.front.basket.update_methods:BasketUpdateMethods")

#: Spec string for the basket class used in the frontend.
#:
#: This is used to customize the behavior of the basket for a given installation,
#: for instance to modify prices of products based on certain conditions, etc.
E-Commerce_BASKET_CLASS_SPEC = (
    "E-Commerce.front.basket.objects:BaseBasket")

#: The spec string defining which basket storage class to use for the frontend.
#:
#: Basket storages are responsible for persisting visitor basket state,
#: the default stores the basket to database (DatabaseBasketStorage)
#: Custom storage backends could use caches, flat files, etc. if required.
E-Commerce_BASKET_STORAGE_CLASS_SPEC = (
    "E-Commerce.front.basket.storage:DatabaseBasketStorage")

#: Spec string for the Django CBV (or an API-compliant class) for the checkout view.
#:
#: This is used to customize the behavior of the checkout process; most likely to
#: switch in a view with a different ``phase_specs``.
E-Commerce_CHECKOUT_VIEW_SPEC = (
    "E-Commerce.front.views.checkout:DefaultCheckoutView")

#: Default product lists facet configuration
#:
#: This configuration will be used if the configuration is not set from admin
E-Commerce_FRONT_DEFAULT_SORT_CONFIGURATION = {
    "sort_products_by_name": True,
    "sort_products_by_name_ordering": 1,
    "sort_products_by_price": True,
    "sort_products_by_price_ordering": 2
}

#: Default cache duration for template helpers
#:
#: Cache duration in seconds for front template helpers. Default 30 minutes.
E-Commerce_TEMPLATE_HELPERS_CACHE_DURATION = 60*30

#: A dictionary defining properties to override the default field properties of the
#: person contact form. Should map the field name (as a string) to a dictionary
#: containing the overriding Django form field properties, as in the following
#: example which makes the gender field hidden:
#:
#: E-Commerce_PERSON_CONTACT_FIELD_PROPERTIES = {
#:    "gender": {"widget": forms.HiddenInput()}
#: }
#:
#: It should be noted, however, that overriding some settings (such as making a
#: required field non-required) could create other validation issues.
E-Commerce_PERSON_CONTACT_FIELD_PROPERTIES = {}

#: A dictionary defining properties to override the default field properties of the
#: confirm form. Should map the field name (as a string) to a dictionary
#: containing the overriding Django form field properties, as in the following
#: example which makes the gender field hidden:
#:
#: E-Commerce_CHECKOUT_CONFIRM_FORM_PROPERTIES = {
#:    "marketing": {"initial": True},
#:    "comment": {"widget": forms.HiddenInput()}
#: }
#:
#: It should be noted, however, that overriding some settings (such as making a
#: required field non-required) could create other validation issues.
E-Commerce_CHECKOUT_CONFIRM_FORM_PROPERTIES = {}

#: E-Commerce powered by default content. This content is rendered in theme bottom
#: by default at E-Commerce.front.templates.E-Commerce.front.macros.footer.jinja
E-Commerce_FRONT_POWERED_BY_CONTENT = """
    <p class="powered">Powered by <a target="_blank" href="https://E-Commerce.com">E-Commerce</a></p>
""".strip()


#: Override sort and filters labels with your own.
#:
#: Define dictionary with field identifier as key and new label as value.
#:
#: E-Commerce_FRONT_OVERRIDE_SORTS_AND_FILTERS_LABELS_LOGIC = {
#:      "manufacturers": _("Brands"),
#:      "suppliers": _("Filter by vendor")
#: }
#:
E-Commerce_FRONT_OVERRIDE_SORTS_AND_FILTERS_LABELS_LOGIC = {}
