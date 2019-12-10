# This file is part of E-Commerce.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.


#: Spec string for the Xtheme admin theme context
#:
#: You can use this to determine logic around which themes
#: are visible in your project admin. This function takes shop
#: `E-Commerce.core.models.Shop` and should return `current_theme_classes`
#: and `current_theme` for context where `current_theme_classes`
#: is a list of `E-Commerce.xtheme.models.ThemeSettings`.
E-Commerce_XTHEME_ADMIN_THEME_CONTEXT = (
    "E-Commerce.xtheme.admin_module.utils.get_theme_context"
)

#: Spec to control Xtheme resource injections
#:
#: Include your template names here to prevent xtheme
#: injecting resources. This does not expect the template
#: to exist.
#:
#: Can be useful in situations when you have html and body
#: HTML tags inside the actual template structure.
E-Commerce_XTHEME_EXCLUDE_TEMPLATES_FROM_RESOUCE_INJECTION = [
    "notify/admin/script_item_editor.jinja",
]