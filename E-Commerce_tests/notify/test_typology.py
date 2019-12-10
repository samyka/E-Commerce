# -*- coding: utf-8 -*-
# This file is part of E-Commerce.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from E-Commerce.notify.base import Binding
from E-Commerce.notify.enums import StepConditionOperator
from E-Commerce.notify.script import Context
from E-Commerce.notify.typology import Enum, Language, Model, Text
from E-Commerce_tests.utils import empty_iterable

from .fixtures import ATestEvent


def test_simple_type_matching():
    assert Binding("x", type=Language).get_matching_types(ATestEvent.variables) == {"order_language"}


def test_text_type_matches_all():
    assert Binding("x", type=Text).get_matching_types(ATestEvent.variables) == set(ATestEvent.variables.keys())


def test_model_type_matching():
    assert empty_iterable(Binding("x", type=Model("E-Commerce.Contact")).get_matching_types(ATestEvent.variables))
    assert Binding("x", type=Model("E-Commerce.Order")).get_matching_types(ATestEvent.variables) == {"order"}


def test_enum_type():
    enum_type = Enum(StepConditionOperator)
    assert enum_type.unserialize(StepConditionOperator.ANY) == StepConditionOperator.ANY
    assert enum_type.unserialize("any") == StepConditionOperator.ANY
    assert not enum_type.unserialize("herp")


def test_binding_fallthrough():
    ctx = Context.from_variables()
    b = Binding("x", default="foo")
    assert b.get_value(ctx, {"variable": "var"}) == "foo"
    assert b.get_value(ctx, {}) == "foo"