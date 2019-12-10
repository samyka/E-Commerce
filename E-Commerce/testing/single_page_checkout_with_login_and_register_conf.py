# This file is part of E-Commerce.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from E-Commerce.front.views.checkout import SinglePageCheckoutView


class SinglePageCheckoutViewWithLoginAndRegister(SinglePageCheckoutView):
    initial_phase = "checkout_method"
    phase_specs = [
        "E-Commerce.front.checkout.checkout_method:CheckoutMethodPhase",
        "E-Commerce.front.checkout.checkout_method:RegisterPhase",
        "E-Commerce.front.checkout.addresses:AddressesPhase",
        "E-Commerce.front.checkout.methods:MethodsPhase",
        "E-Commerce.front.checkout.methods:ShippingMethodPhase",
        "E-Commerce.front.checkout.methods:PaymentMethodPhase",
        "E-Commerce.front.checkout.confirm:ConfirmPhase",
    ]
    empty_phase_spec = "E-Commerce.front.checkout.empty:EmptyPhase"


urlpatterns = [
    url(r'^checkout/$', SinglePageCheckoutViewWithLoginAndRegister.as_view(), name='checkout'),
    url(r'^checkout/(?P<phase>.+)/$', SinglePageCheckoutViewWithLoginAndRegister.as_view(), name='checkout'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^sa/', include('E-Commerce.admin.urls', namespace="E-Commerce_admin", app_name="E-Commerce_admin")),
    url(r'^api/', include('E-Commerce.api.urls')),
    url(r'^', include('E-Commerce.front.urls', namespace="E-Commerce", app_name="E-Commerce")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
