# This file is part of E-Commerce.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

"""
Modify these only for E-Commerce tests. For testing modify urls.py instead.
"""
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^sa/', include('E-Commerce.admin.urls', namespace="E-Commerce_admin", app_name="E-Commerce_admin")),
    url(r'^api/', include('E-Commerce.api.urls')),
    url(r'^', include('E-Commerce.front.urls', namespace="E-Commerce", app_name="E-Commerce")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
