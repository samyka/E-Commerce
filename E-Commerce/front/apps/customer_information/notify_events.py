# -*- coding: utf-8 -*-
# This file is part of E-Commerce.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from django.utils.translation import ugettext_lazy as _

from E-Commerce.notify.base import Event, Variable
from E-Commerce.notify.typology import Email, Model


class CompanyAccountCreated(Event):
    identifier = "company_account_created"

    contact = Variable("CompanyContact", type=Model("E-Commerce.CompanyContact"))
    customer_email = Variable(_("Customer Email"), type=Email)
