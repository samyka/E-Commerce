# This file is part of E-Commerce.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
import pytest
from django.utils.encoding import force_text

from E-Commerce.admin.module_registry import replace_modules
from E-Commerce.admin.modules.currencies import CurrencyModule
from E-Commerce.admin.modules.currencies.views import CurrencyEditView
from E-Commerce.testing.factories import get_default_currency, get_default_shop
from E-Commerce.testing.utils import apply_request_middleware


@pytest.mark.django_db
def test_currency_edit_view_works_at_all(rf, admin_user):
    get_default_shop()  # We need a shop to exists
    request = apply_request_middleware(rf.get("/"), user=admin_user)
    request.user = admin_user

    currency = get_default_currency()

    with replace_modules([CurrencyModule]):
        view_func = CurrencyEditView.as_view()
        response = view_func(request, pk=currency.pk)
        response.render()
        assert (currency.code in force_text(response.content))
        response = view_func(request, pk=None)  # "new mode"
        response.render()
        assert response.content