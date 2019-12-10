# -*- coding: utf-8 -*-
# This file is part of E-Commerce.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from __future__ import unicode_literals

import json
import base64
import os
from django.utils.translation import activate
from rest_framework import status
from rest_framework.test import APIClient

from E-Commerce.core import cache
from E-Commerce.core.models import Category, CategoryStatus, CategoryVisibility
from E-Commerce.testing.factories import get_default_shop, get_random_filer_image


def setup_function(fn):
    cache.clear()


def test_category_api(admin_user):
    activate("en")
    shop = get_default_shop()
    client = APIClient()
    client.force_authenticate(user=admin_user)
    image = get_random_filer_image()
    with open(image.path, 'rb') as f:
        img_base64 = base64.b64encode(os.urandom(50)).decode()
        uri = "data:application/octet-stream;base64,{}".format(img_base64)
    category_data = {
        "shops": [shop.pk],
        "status": CategoryStatus.VISIBLE.value,
        "ordering": 1,
        "visibility": CategoryVisibility.VISIBLE_TO_ALL.value,
        "visible_in_menu": True,
        "translations": {"en": {"name": "Category 1"}},
        "image_path" : "/didnt/choose/path",
        "image" : uri
    }
    response = client.post("/api/E-Commerce/category/",
                           content_type="application/json",
                           data=json.dumps(category_data))
    assert response.status_code == status.HTTP_201_CREATED
    category = Category.objects.first()
    assert category.name == category_data["translations"]["en"]["name"]
    assert category.status.value == category_data["status"]
    assert category.ordering == category_data["ordering"]
    assert category.visibility.value == category_data["visibility"]
    assert category.visible_in_menu == category_data["visible_in_menu"]
    assert category.shops.first().pk == shop.pk
    assert category.image.folder.pretty_logical_path == category_data["image_path"]

    with open(category.image.path, 'rb') as f:
        assert img_base64 == base64.b64encode(f.read()).decode()

    category_data.pop("image_path") # Test error when not sending a path
    response = client.post("/api/E-Commerce/category/",
                           content_type="application/json",
                           data=json.dumps(category_data))
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    data = json.loads(response.content.decode("utf-8"))
    assert data["non_field_errors"][0] == "Path is required when sending a Category image."

    category_data["image_path"] = "/path/chose/me"
    category_data["translations"]["en"]["name"] = "name 2"
    category_data["ordering"] = 3

    response = client.put("/api/E-Commerce/category/%d/" % category.id,
                          content_type="application/json",
                          data=json.dumps(category_data))
    assert response.status_code == status.HTTP_200_OK
    category = Category.objects.first()
    assert category.name == category_data["translations"]["en"]["name"]
    assert category.ordering == category_data["ordering"]

    response = client.get("/api/E-Commerce/category/%d/" % category.id)
    assert response.status_code == status.HTTP_200_OK
    data = json.loads(response.content.decode("utf-8"))
    assert category.name == data["translations"]["en"]["name"]
    assert category.status.value == data["status"]
    assert category.ordering == data["ordering"]
    assert category.visibility.value == data["visibility"]
    assert category.visible_in_menu == data["visible_in_menu"]

    response = client.get("/api/E-Commerce/category/")
    assert response.status_code == status.HTTP_200_OK
    data = json.loads(response.content.decode("utf-8"))
    assert category.name == data[0]["translations"]["en"]["name"]
    assert category.ordering == data[0]["ordering"]

    response = client.get("/api/E-Commerce/category/?status=%s" % CategoryStatus.VISIBLE.value)
    assert response.status_code == status.HTTP_200_OK
    data = json.loads(response.content.decode("utf-8"))
    assert len(data) == 1

    response = client.get("/api/E-Commerce/category/?status=%s" % CategoryStatus.INVISIBLE.value)
    assert response.status_code == status.HTTP_200_OK
    data = json.loads(response.content.decode("utf-8"))
    assert len(data) == 0

    response = client.get("/api/E-Commerce/category/?status=%s" % CategoryStatus.DELETED.value)
    assert response.status_code == status.HTTP_200_OK
    data = json.loads(response.content.decode("utf-8"))
    assert len(data) == 0

    # soft delete
    response = client.delete("/api/E-Commerce/category/%d/" % category.id)
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Category.objects.first().status == CategoryStatus.DELETED

    response = client.get("/api/E-Commerce/category/?status=%s" % CategoryStatus.DELETED.value)
    assert response.status_code == status.HTTP_200_OK
    data = json.loads(response.content.decode("utf-8"))
    assert len(data) == 1
