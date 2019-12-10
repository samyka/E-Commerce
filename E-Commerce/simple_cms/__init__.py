# This file is part of E-Commerce.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _

import E-Commerce.apps


class AppConfig(E-Commerce.apps.AppConfig):
    name = __name__
    verbose_name = _("Content Pages")
    label = "E-Commerce_simple_cms"

    provides = {
        "front_urls_post": [__name__ + ".urls:urlpatterns"],
        "admin_module": [
            "E-Commerce.simple_cms.admin_module:SimpleCMSAdminModule"
        ],
        "front_template_helper_namespace": [
            "E-Commerce.simple_cms.template_helpers:SimpleCMSTemplateHelpers"
        ],
        "xtheme_layout": [
            "E-Commerce.simple_cms.layout:PageLayout",
        ],
        "xtheme_plugin": [
            "E-Commerce.simple_cms.plugins:PageLinksPlugin"
        ],
        "simple_cms_template": [
            "E-Commerce.simple_cms.templates:SimpleCMSDefaultTemplate",
            "E-Commerce.simple_cms.templates:SimpleCMSTemplateSidebar",
        ],
        "admin_page_form_part": [
            "E-Commerce.simple_cms.admin_module.form_parts:CMSOpenGraphFormPart"
        ]
    }

    def ready(self):
        from E-Commerce.simple_cms.models import Page
        import reversion
        reversion.register(Page._parler_meta.root_model)


default_app_config = __name__ + ".AppConfig"
