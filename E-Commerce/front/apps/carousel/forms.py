# -*- coding: utf-8 -*-
# This file is part of E-Commerce.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from django.forms import BooleanField
from django.utils.translation import ugettext_lazy as _

from E-Commerce.admin.shop_provider import get_shop
from E-Commerce.front.apps.carousel.models import Carousel
from E-Commerce.xtheme.plugins.forms import GenericPluginForm
from E-Commerce.xtheme.plugins.widgets import XThemeModelChoiceField


class CarouselConfigForm(GenericPluginForm):
    def populate(self):
        super(CarouselConfigForm, self).populate()
        self.fields["carousel"] = XThemeModelChoiceField(
            label=_("Carousel"),
            queryset=Carousel.objects.filter(shops=get_shop(self.request)),
            required=False,
        )
        self.fields["active"] = BooleanField(
            label=_("Active"),
            required=False,
        )

    def clean(self):
        cleaned_data = super(CarouselConfigForm, self).clean()
        carousel = cleaned_data.get("carousel")
        cleaned_data["carousel"] = carousel.pk if hasattr(carousel, "pk") else None
        return cleaned_data
