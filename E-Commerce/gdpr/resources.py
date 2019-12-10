# -*- coding: utf-8 -*-
# This file is part of E-Commerce.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from django.conf import settings
from django.template import loader
from rest_framework.reverse import reverse

from E-Commerce.core.shop_provider import get_shop
from E-Commerce.core.utils.static import get_E-Commerce_static_url
from E-Commerce.gdpr.models import GDPRCookieCategory, GDPRSettings
from E-Commerce.gdpr.utils import (
    get_active_consent_pages, get_privacy_policy_page,
    should_reconsent_privacy_policy
)
from E-Commerce.utils.djangoenv import has_installed
from E-Commerce.xtheme.resources import add_resource, InlineMarkupResource


def valid_view(context):
    view_class = getattr(context["view"], "__class__", None) if context.get("view") else None
    if not view_class or not context.get("request"):
        return False

    request = context.get("request")
    if request:
        match = request.resolver_match
        if match and match.app_name == "E-Commerce_admin":
            return False

    view_name = getattr(view_class, "__name__", "")
    if view_name == "EditorView":
        return False

    return True


def add_gdpr_consent_resources(context, content):
    if not valid_view(context):
        return

    request = context["request"]
    shop = get_shop(request)
    gdpr_settings = GDPRSettings.get_for_shop(shop)

    # GDPR not enabled, nothing to do
    if not gdpr_settings.enabled:
        return

    # always add styles
    add_resource(context, "head_end", get_E-Commerce_static_url("E-Commerce-gdpr.css"))

    user = request.user
    if not user.is_anonymous() and should_reconsent_privacy_policy(shop, user):
        consent_page = get_privacy_policy_page(shop)
        render_context = {
            "request": request,
            "csrf_token": context["csrf_token"],
            "url": "/%s" % consent_page.url,
            "accept_url": reverse("E-Commerce:gdpr_policy_consent", kwargs=dict(page_id=consent_page.id))
        }
        update_resource = InlineMarkupResource(
            loader.render_to_string("E-Commerce/gdpr/privacy_policy_update.jinja", context=render_context)
        )
        add_resource(context, "body_end", update_resource)

    # consent already added
    if settings.E-Commerce_GDPR_CONSENT_COOKIE_NAME in request.COOKIES:
        return

    gdpr_documents = []
    if has_installed("E-Commerce.simple_cms"):
        gdpr_documents = get_active_consent_pages(shop)

    render_context = {
        "request": request,
        "csrf_token": context["csrf_token"],
        "gdpr_settings": gdpr_settings,
        "gdpr_documents": gdpr_documents,
        "gdpr_cookie_categories": GDPRCookieCategory.objects.filter(shop=shop)
    }
    html_resource = InlineMarkupResource(
        loader.render_to_string("E-Commerce/gdpr/gdpr_consent.jinja", context=render_context)
    )
    add_resource(context, "body_end", html_resource)
    add_resource(context, "body_end", get_E-Commerce_static_url("E-Commerce-gdpr.js"))
