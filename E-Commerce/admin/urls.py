# -*- coding: utf-8 -*-
# This file is part of E-Commerce.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.

from __future__ import unicode_literals

import warnings

import django.contrib.auth.views as auth_views
from django.conf.urls import url
from django.contrib.auth import logout as do_logout
from django.views.decorators.csrf import csrf_exempt
from django.views.i18n import set_language

from E-Commerce.admin.forms import EmailAuthenticationForm
from E-Commerce.admin.module_registry import get_module_urls
from E-Commerce.admin.utils.urls import admin_url, AdminRegexURLPattern
from E-Commerce.admin.views.dashboard import DashboardView
from E-Commerce.admin.views.edit import EditObjectView
from E-Commerce.admin.views.home import HomeView
from E-Commerce.admin.views.menu import MenuToggleView, MenuView
from E-Commerce.admin.views.password import RequestPasswordView, ResetPasswordView
from E-Commerce.admin.views.search import SearchView
from E-Commerce.admin.views.select import MultiselectAjaxView
from E-Commerce.admin.views.tour import TourView
from E-Commerce.admin.views.wizard import WizardView
from E-Commerce.utils.i18n import javascript_catalog_all


def login(request, **kwargs):
    if not request.user.is_anonymous() and request.method == "POST":  # We're logging in, so log out first
        do_logout(request)
    kwargs.setdefault("extra_context", {})["error"] = request.GET.get("error")
    return auth_views.login(request, authentication_form=EmailAuthenticationForm, **kwargs)


def get_urls():
    urls = []
    urls.extend(get_module_urls())

    urls.extend([
        admin_url(r'^$', DashboardView.as_view(), name='dashboard', permissions=()),
        admin_url(r'^home/$', HomeView.as_view(), name='home', permissions=()),
        admin_url(r'^wizard/$', WizardView.as_view(), name='wizard', permissions=()),
        admin_url(r'^tour/$', TourView.as_view(), name='tour', permissions=()),
        admin_url(r'^search/$', SearchView.as_view(), name='search', permissions=()),
        admin_url(r'^select/$', MultiselectAjaxView.as_view(), name='select', permissions=()),
        admin_url(r'^edit/$', EditObjectView.as_view(), name='edit', permissions=()),
        admin_url(r'^menu/$', MenuView.as_view(), name='menu', permissions=()),
        admin_url(r'^toggle-menu/$', MenuToggleView.as_view(), name='menu_toggle', permissions=()),
        admin_url(
            r'^login/$',
            login,
            kwargs={"template_name": "E-Commerce/admin/auth/login.jinja"},
            name='login',
            require_authentication=False,
            permissions=()
        ),
        admin_url(
            r'^logout/$',
            auth_views.logout,
            kwargs={"template_name": "E-Commerce/admin/auth/logout.jinja"},
            name='logout',
            require_authentication=False,
            permissions=()
        ),
        admin_url(
            r'^recover-password/(?P<uidb64>.+)/(?P<token>.+)/$',
            ResetPasswordView,
            name='recover_password',
            require_authentication=False,
            permissions=()
        ),
        admin_url(
            r'^request-password/$',
            RequestPasswordView,
            name='request_password',
            require_authentication=False,
            permissions=()
        ),
        admin_url(
            r'^set-language/$',
            csrf_exempt(set_language),
            name="set-language",
            permissions=()
        ),
    ])

    for u in urls:  # pragma: no cover
        if not isinstance(u, AdminRegexURLPattern):
            warnings.warn("Admin URL %r is not an AdminRegexURLPattern" % u)

    # Add Django javascript catalog url
    urls.append(url(r'^i18n.js$', javascript_catalog_all, name='js-catalog'))

    return tuple(urls)


urlpatterns = get_urls()
