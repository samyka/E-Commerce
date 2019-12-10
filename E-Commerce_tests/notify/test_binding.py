# -*- coding: utf-8 -*-
# This file is part of E-Commerce.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
import pytest

from E-Commerce.notify.script import Context
from E-Commerce.notify.actions import AddNotification
from E-Commerce.notify.base import TemplatedBinding
from E-Commerce.notify.enums import ConstantUse


def test_templated_binding_security():
    with pytest.raises(ValueError):
        tb = TemplatedBinding("x", constant_use=ConstantUse.VARIABLE_ONLY)

    with pytest.raises(ValueError):
        tb = TemplatedBinding("y", constant_use=ConstantUse.VARIABLE_OR_CONSTANT)


def test_templated_binding_syntax_errors_swallowed():
    tb = TemplatedBinding("z", constant_use=ConstantUse.CONSTANT_ONLY)
    assert tb.get_value(Context(), {"constant": "{{"}) == "{{"


def test_bind_verification():
    with pytest.raises(ValueError):
        AddNotification({})  # add_notification requires a binding for message
