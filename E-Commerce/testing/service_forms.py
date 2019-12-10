# This file is part of E-Commerce.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.

from E-Commerce.admin.forms import E-CommerceAdminForm

from .models import (
    CarrierWithCheckoutPhase, PaymentWithCheckoutPhase, PseudoPaymentProcessor
)


class PseudoPaymentProcessorForm(E-CommerceAdminForm):
    class Meta:
        model = PseudoPaymentProcessor
        exclude = ["identifier"]


class PaymentWithCheckoutPhaseForm(E-CommerceAdminForm):
    class Meta:
        model = PaymentWithCheckoutPhase
        exclude = ["identifier"]


class CarrierWithCheckoutPhaseForm(E-CommerceAdminForm):
    class Meta:
        model = CarrierWithCheckoutPhase
        exclude = ["identifier"]
