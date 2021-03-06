# -*- coding: utf-8 -*-
# This file is part of E-Commerce.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
import pytest
import six
from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse, reverse_lazy

from E-Commerce.admin.menu import get_menu_entry_categories
from E-Commerce.admin.modules.customers_dashboard import CustomersDashboardModule
from E-Commerce.admin.modules.sales_dashboard import SalesDashboardModule
from E-Commerce.admin.module_registry import get_modules, replace_modules
from E-Commerce.admin.toolbar import (
    DropdownActionButton, DropdownItem, JavaScriptActionButton,
    PostActionButton, URLActionButton,
    NewActionButton, SettingsActionButton)
from E-Commerce.admin.utils.permissions import (
    get_default_model_permissions, get_permission_object_from_string,
    get_permissions_from_urls, set_permissions_for_group
)
from E-Commerce.core.models import Product, ShopProduct
from E-Commerce.testing import factories
from E-Commerce_tests.admin.fixtures.test_module import ARestrictedTestModule
from E-Commerce_tests.utils.faux_users import StaffUser


migrated_permissions = {
    CustomersDashboardModule: ("E-Commerce.view_customers_dashboard"),
    SalesDashboardModule: ("E-Commerce.view_sales_dashboard"),
}


def test_default_model_permissions():
    permissions = set(["E-Commerce.add_product", "E-Commerce.delete_product", "E-Commerce.change_product"])

    assert get_default_model_permissions(Product) == permissions


def test_permissions_for_menu_entries(rf, admin_user):
    request = rf.get("/")
    request.user = factories.get_default_staff_user()
    permission_group = request.user.groups.first()
    set_permissions_for_group(
        permission_group,
        set("dashboard") | set(ARestrictedTestModule().get_required_permissions())
    )

    with replace_modules([ARestrictedTestModule]):
        categories = get_menu_entry_categories(request)
        assert categories

        # Make sure category is displayed if user has correct permissions
        test_category_menu_entries = [cat for cat in categories if cat.name == "RestrictedTest"][0]
        assert any(me.text == "OK" for me in test_category_menu_entries)

        # No menu items should be displayed if user has no permissions
        set_permissions_for_group(permission_group, set())
        categories = get_menu_entry_categories(request)
        assert not categories


@pytest.mark.django_db
def test_valid_permissions_for_all_modules():
    """
    If a module requires permissions, make sure all url and module-
    level permissions are valid.

    Modules that add permissions using migrations must be checked
    manually since their permissions will not be in the test database.
    """
    for module in get_modules():
        url_permissions = set(get_permissions_from_urls(module.get_urls()))
        module_permissions = set(module.get_required_permissions())
        for permission in (url_permissions | module_permissions):
            # Only requirement for permissions are that they
            # are list of strings
            assert isinstance(permission, six.string_types)


@pytest.mark.django_db
@pytest.mark.parametrize("button_class, kwargs", [
    (URLActionButton, {"url": "/test/url/"}),
    (JavaScriptActionButton, {"onclick": None}),
    (PostActionButton, {}),
    (DropdownActionButton, {"items": [DropdownItem()]}),
    (DropdownItem, {})
])
def test_toolbar_button_permissions(rf, button_class, kwargs):
    permissions = set(["E-Commerce.add_product", "E-Commerce.delete_product", "E-Commerce.change_product"])

    request = rf.get("/")
    request.user = factories.get_default_staff_user()
    button = button_class(required_permissions=permissions, **kwargs)
    rendered_button = "".join(bit for bit in button.render(request))
    assert not rendered_button

    # Set permissions for the user
    set_permissions_for_group(request.user.groups.first(), permissions)
    rendered_button = "".join(bit for bit in button.render(request))
    assert rendered_button


@pytest.mark.parametrize("button, permission, instance", [
    (URLActionButton(url=reverse("E-Commerce_admin:shop_product.new")), "shop_product.new", URLActionButton),
    (URLActionButton(url=reverse_lazy("E-Commerce_admin:shop_product.new")), "shop_product.new", URLActionButton),

    (NewActionButton.for_model(ShopProduct), "shop_product.new", URLActionButton),
    (SettingsActionButton.for_model(ShopProduct, return_url="/"), "shop_product.list_settings", URLActionButton),

    # for_model without E-Commerce_admin url returns None
    (NewActionButton.for_model(AbstractUser), "abstract_user.new", type(None)),
    (SettingsActionButton.for_model(AbstractUser), "abstract_user.list_settings", type(None)),
])
def test_url_buttons_permission(rf, button, permission, instance):
    request = rf.get("/")

    assert isinstance(button, instance)

    if button is not None:
        request.user = factories.get_default_staff_user()
        assert not "".join(bit for bit in button.render(request))

        set_permissions_for_group(request.user.groups.first(), (permission,))
        assert "".join(bit for bit in button.render(request))
