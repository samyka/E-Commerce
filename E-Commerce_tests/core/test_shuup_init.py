# -*- coding: utf-8 -*-
# This file is part of E-Commerce.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
import pytest

from django.core.management import call_command
from django.utils.translation import activate
from E-Commerce.core.models import Currency, Shop, Supplier


@pytest.mark.django_db
def test_E-Commerce_init():
    activate("en")
    assert Currency.objects.count() == 1
    assert Shop.objects.filter(identifier="default").exists()  # Tests init
    assert not Supplier.objects.first()
    call_command("E-Commerce_init")
    assert Supplier.objects.first()
    assert Currency.objects.count() == 7
