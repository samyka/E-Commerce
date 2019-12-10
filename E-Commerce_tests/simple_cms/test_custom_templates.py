# This file is part of E-Commerce.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
import datetime

import pytest

from E-Commerce.simple_cms.models import Page
from E-Commerce.simple_cms.views import PageView
from E-Commerce.testing.factories import get_default_shop
from E-Commerce.testing.utils import apply_request_middleware
from E-Commerce_tests.simple_cms.utils import create_page


@pytest.mark.django_db
@pytest.mark.parametrize("template_name", ["page.jinja", "page_sidebar.jinja"])
def test_superuser_can_see_invisible_page(rf, template_name):
    template_path = 'E-Commerce/simple_cms/' + template_name
    page = create_page(template_name=template_path, available_from=datetime.date(1988, 1, 1), shop=get_default_shop())
    view_func = PageView.as_view()
    request = apply_request_middleware(rf.get("/"))
    response = view_func(request, url=page.url)
    response.render()
    assert response.template_name[0] == template_path
