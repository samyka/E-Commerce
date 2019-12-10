# This file is part of E-Commerce.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from E-Commerce.apps import AppConfig
from E-Commerce.utils import update_module_attributes

from ._theme import (
    get_current_theme, get_middleware_current_theme, get_theme_by_identifier,
    get_theme_cache_key, set_current_theme, set_middleware_current_theme,
    Theme
)
from .plugins._base import Plugin, templated_plugin_factory, TemplatedPlugin

__all__ = [
    "Plugin",
    "TemplatedPlugin",
    "Theme",
    "get_current_theme",
    "get_theme_by_identifier",
    "set_current_theme",
    "templated_plugin_factory",
    "get_theme_cache_key",
    "get_middleware_current_theme",
    "set_middleware_current_theme"
]

XTHEME_GLOBAL_VIEW_NAME = "_XthemeGlobalView"


class XThemeAppConfig(AppConfig):
    name = "E-Commerce.xtheme"
    verbose_name = "E-Commerce Extensible Theme Engine"
    label = "E-Commerce_xtheme"

    provides = {
        "front_urls_pre": [__name__ + ".urls:urlpatterns"],
        "xtheme_plugin": [
            "E-Commerce.xtheme.plugins.image:ImagePlugin",
            "E-Commerce.xtheme.plugins.category_links:CategoryLinksPlugin",
            "E-Commerce.xtheme.plugins.products:ProductsFromCategoryPlugin",
            "E-Commerce.xtheme.plugins.products:ProductHighlightPlugin",
            "E-Commerce.xtheme.plugins.products:ProductCrossSellsPlugin",
            "E-Commerce.xtheme.plugins.products:ProductSelectionPlugin",
            "E-Commerce.xtheme.plugins.snippets:SnippetsPlugin",
            "E-Commerce.xtheme.plugins.social_media_links:SocialMediaLinksPlugin",
            "E-Commerce.xtheme.plugins.text:TextPlugin",
        ],
        "xtheme_layout": [
            "E-Commerce.xtheme.layout.ProductLayout",
            "E-Commerce.xtheme.layout.CategoryLayout",
            "E-Commerce.xtheme.layout.AnonymousContactLayout",
            "E-Commerce.xtheme.layout.ContactLayout",
            "E-Commerce.xtheme.layout.PersonContactLayout",
            "E-Commerce.xtheme.layout.CompanyContactLayout",
        ],
        "admin_module": [
            "E-Commerce.xtheme.admin_module:XthemeAdminModule",
            "E-Commerce.xtheme.admin_module:XthemeSnippetsAdminModule"
        ],
        "xtheme_resource_injection": [
            "E-Commerce.xtheme.resources:inject_global_snippet"
        ],
    }


default_app_config = "E-Commerce.xtheme.XThemeAppConfig"

update_module_attributes(__all__, __name__)
