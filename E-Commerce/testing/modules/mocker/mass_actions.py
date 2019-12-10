# -*- coding: utf-8 -*-
# This file is part of E-Commerce.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _

from E-Commerce.admin.utils.picotable import (
    PicotableMassAction, PicotableMassActionProvider
)


class DummyPicotableMassAction1(PicotableMassAction):
    label = _("Dummy Mass Action #1")
    identifier = "dummy_mass_action_1"


class DummyPicotableMassAction2(PicotableMassAction):
    label = _("Dummy Mass Action #2")
    identifier = "dummy_mass_action_2"


class DummyMassActionProvider(PicotableMassActionProvider):
    @classmethod
    def get_mass_actions_for_view(cls, view):
        return [
            "E-Commerce.testing.modules.mocker.mass_actions:DummyPicotableMassAction1",
            "E-Commerce.testing.modules.mocker.mass_actions:DummyPicotableMassAction2"
        ]
