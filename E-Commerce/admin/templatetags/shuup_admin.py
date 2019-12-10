# -*- coding: utf-8 -*-
# This file is part of E-Commerce.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.

from bootstrap3.renderers import FormRenderer
from django.utils.safestring import mark_safe
from django_jinja import library

from E-Commerce.admin.template_helpers import \
    E-Commerce_admin as E-Commerce_admin_template_helpers
from E-Commerce.admin.utils.bs3_renderers import AdminFieldRenderer


class Bootstrap3Namespace(object):
    def field(self, field, **kwargs):
        if not field:
            return ""
        return mark_safe(AdminFieldRenderer(field, **kwargs).render())

    def form(self, form, **kwargs):
        return mark_safe(FormRenderer(form, **kwargs).render())


library.global_function(name="E-Commerce_admin", fn=E-Commerce_admin_template_helpers)
library.global_function(name="bs3", fn=Bootstrap3Namespace())
