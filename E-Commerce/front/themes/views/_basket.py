# -*- coding: utf-8 -*-
# This file is part of E-Commerce.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from django.http import HttpResponse
from django.template.loader import render_to_string


def basket_partial(request):
    return HttpResponse(
        render_to_string(
            "E-Commerce/front/basket/navigation_basket_partial.jinja",
            request=request,
        )
    )
