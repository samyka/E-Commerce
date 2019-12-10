# -*- coding: utf-8 -*-
# This file is part of E-Commerce.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.

import django.conf
from django import forms
from django.utils.encoding import force_text
from django.utils.translation import ugettext_lazy as _

from E-Commerce.front.themes import BaseThemeFieldsMixin
from E-Commerce.xtheme import Theme


class ClassicGrayTheme(BaseThemeFieldsMixin, Theme):
    identifier = "E-Commerce.themes.classic_gray"
    name = "E-Commerce Classic Gray Theme"
    author = "E-Commerce Team"
    template_dir = "classic_gray"
    guide_template = "classic_gray/admin/guide.jinja"
    stylesheets = [
        {
            "identifier": "default",
            "stylesheet": "E-Commerce/front/css/style.css",
            "name": _("Default"),
            "images": ["E-Commerce/front/img/no_image.png"]
        },
        {
            "identifier": "midnight_blue",
            "stylesheet": "E-Commerce/classic_gray/blue/style.css",
            "name": _("Midnight Blue"),
            "images": ["E-Commerce/front/img/no_image.png"]
        },
        {
            "identifier": "candy_pink",
            "stylesheet": "E-Commerce/classic_gray/pink/style.css",
            "name": _("Candy Pink"),
            "images": ["E-Commerce/front/img/no_image.png"]
        },
    ]

    _theme_fields = [
        ("show_welcome_text", forms.BooleanField(required=False, initial=True, label=_("Show Frontpage Welcome Text")))
    ]

    @property
    def fields(self):
        return self._theme_fields + super(ClassicGrayTheme, self).get_base_fields()

    def get_view(self, view_name):
        import E-Commerce.front.themes.views as views
        return getattr(views, view_name, None)

    def _format_cms_links(self, shop, **query_kwargs):
        if "E-Commerce.simple_cms" not in django.conf.settings.INSTALLED_APPS:
            return
        from E-Commerce.simple_cms.models import Page
        for page in Page.objects.visible(shop).filter(**query_kwargs):
            yield {"url": "/%s" % page.url, "text": force_text(page)}

    def get_cms_navigation_links(self, request):
        return self._format_cms_links(shop=request.shop, visible_in_menu=True)
