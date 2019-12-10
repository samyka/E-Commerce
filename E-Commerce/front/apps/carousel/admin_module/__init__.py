# -*- coding: utf-8 -*-
# This file is part of E-Commerce.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _

from E-Commerce.admin.base import AdminModule, MenuEntry
from E-Commerce.admin.menu import CONTENT_MENU_CATEGORY
from E-Commerce.admin.utils.urls import (
    admin_url, derive_model_url, get_edit_and_list_urls
)
from E-Commerce.front.apps.carousel.models import Carousel


class CarouselModule(AdminModule):
    name = _("Carousels")
    breadcrumbs_menu_entry = MenuEntry(text=name, url="E-Commerce_admin:carousel.list", category=CONTENT_MENU_CATEGORY)

    def get_urls(self):
        return get_edit_and_list_urls(
            url_prefix="^carousels",
            view_template="E-Commerce.front.apps.carousel.admin_module.views.Carousel%sView",
            name_template="carousel.%s"
        ) + [
            admin_url(
                "^carousel/(?P<pk>\d+)/delete/$",
                "E-Commerce.front.apps.carousel.admin_module.views.CarouselDeleteView",
                name="carousel.delete"
            ),
        ]

    def get_menu_entries(self, request):
        return [
            MenuEntry(
                text=self.name,
                icon="fa fa-image",
                url="E-Commerce_admin:carousel.list",
                category=CONTENT_MENU_CATEGORY,
            )
        ]

    def get_model_url(self, object, kind, shop=None):
        return derive_model_url(Carousel, "E-Commerce_admin:carousel", object, kind)
