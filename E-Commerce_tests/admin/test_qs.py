# -*- coding: utf-8 -*-
# This file is part of E-Commerce.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from E-Commerce.admin.utils.urls import manipulate_query_string


def test_qs_manipulation():
    url = "http://example.com/"
    assert manipulate_query_string(url) == url  # Noop works
    hello_url = manipulate_query_string(url, q="hello", w="wello")  # Adding works
    assert "q=hello" in hello_url
    assert "w=wello" in hello_url
    unhello_url = manipulate_query_string(hello_url, q=None)  # Removal works
    assert "w=wello" in unhello_url
