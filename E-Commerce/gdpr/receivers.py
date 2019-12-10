# -*- coding: utf-8 -*-
# This file is part of E-Commerce.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from django.dispatch import receiver

from E-Commerce.front.signals import (
    checkout_complete, company_registration_save, login_allowed,
    person_registration_save
)
from E-Commerce.gdpr.utils import create_user_consent_for_all_documents


@receiver(company_registration_save)
def create_consents_company_registration_save(sender, request, user, company, *args, **kwargs):
    create_user_consent_for_all_documents(request.shop, user)


@receiver(person_registration_save)
def create_consents_person_registration_save(sender, request, user, contact, *args, **kwargs):
    create_user_consent_for_all_documents(request.shop, user)


@receiver(login_allowed)
def create_consents_login_allowed(sender, request, user, *args, **kwargs):
    create_user_consent_for_all_documents(request.shop, user)


@receiver(checkout_complete)
def create_consents_checkout_complete(sender, request, user, order, *args, **kwargs):
    create_user_consent_for_all_documents(request.shop, user)
