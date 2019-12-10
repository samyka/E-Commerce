# This file is part of E-Commerce.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.

from E-Commerce.xtheme.admin_module.views._snippet import (
    SnippetDeleteView, SnippetEditView, SnippetListView
)
from E-Commerce.xtheme.admin_module.views._theme import (
    ActivationForm, TemplateView, ThemeConfigDetailView, ThemeConfigView,
    ThemeGuideTemplateView, ThemeWizardPane
)

__all__ = [
    "ActivationForm",
    "SnippetDeleteView",
    "SnippetEditView",
    "SnippetListView",
    "TemplateView",
    "ThemeConfigDetailView",
    "ThemeConfigView",
    "ThemeGuideTemplateView",
    "ThemeWizardPane"
]
