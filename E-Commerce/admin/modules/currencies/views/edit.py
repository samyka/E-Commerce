# This file is part of E-Commerce.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from django import forms

from E-Commerce.admin.utils.views import CreateOrUpdateView
from E-Commerce.core.models import Currency


class CurrencyForm(forms.ModelForm):
    class Meta:
        model = Currency
        exclude = ()


class CurrencyEditView(CreateOrUpdateView):
    model = Currency
    form_class = CurrencyForm
    template_name = "E-Commerce/admin/currencies/edit_currency.jinja"
    context_object_name = "currency"
    add_form_errors_as_messages = True
