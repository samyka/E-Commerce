# This file is part of E-Commerce.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.

import pytest
from django.utils.translation import activate

from E-Commerce.front.views.checkout import BaseCheckoutView
from E-Commerce.testing.utils import apply_request_middleware


class CheckoutMethodsOnlyCheckoutView(BaseCheckoutView):
    phase_specs = ['E-Commerce.front.checkout.checkout_method:CheckoutMethodPhase']


@pytest.mark.django_db
def test_checkout_method_phase_basic(rf):
    activate("en")
    view = CheckoutMethodsOnlyCheckoutView.as_view()

    request = apply_request_middleware(rf.get("/"))
    response = view(request=request, phase='checkout_method')
    if hasattr(response, "render"):
        response.render()
    assert response.status_code == 200
