# -*- coding: utf-8 -*-
import django


class DisableMigrations(object):
    # See https://gist.github.com/NotSqrt/5f3c76cd15e40ef62d09
    def __contains__(self, item):
        return True

    def __getitem__(self, item):
        return "notmigrations"


def get_disabled_migrations():
    if django.VERSION < (1, 11):
        return DisableMigrations()

    return {
        'auth': None,
        'contenttypes': None,
        'default': None,
        'sessions': None,

        'E-Commerce': None,
        'E-Commerce_admin': None,
        'default_tax': None,
        'E-Commerce_front': None,
        'carousel': None,
        'E-Commerce_notify': None,
        'E-Commerce_simple_cms': None,
        'simple_supplier': None,
        'E-Commerce_customer_group_pricing': None,
        'campaigns': None,
        'E-Commerce_xtheme': None,
        'E-Commerce_testing': None,
        'E-Commerce_gdpr': None,
        'E-Commerce_tasks': None,
        'discounts': None,

        'django_countries': None,
        'filer': None,
        'reversion': None
    }
