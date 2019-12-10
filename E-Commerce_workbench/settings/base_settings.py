# This file is part of E-Commerce.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
import os

from E-Commerce.addons import add_enabled_addons

BASE_DIR = os.getenv("E-Commerce_WORKBENCH_BASE_DIR") or (
    os.path.dirname(os.path.dirname(__file__)))
SECRET_KEY = "Shhhhh"
DEBUG = True
ALLOWED_HOSTS = ["*"]

MEDIA_ROOT = os.path.join(BASE_DIR, "var", "media")
STATIC_ROOT = os.path.join(BASE_DIR, "var", "static")
MEDIA_URL = "/media/"

E-Commerce_ENABLED_ADDONS_FILE = os.getenv("E-Commerce_ENABLED_ADDONS_FILE") or (
    os.path.join(BASE_DIR, "var", "enabled_addons"))

INSTALLED_APPS = add_enabled_addons(E-Commerce_ENABLED_ADDONS_FILE, [
    # django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    # external apps that needs to be loaded before E-Commerce
    'easy_thumbnails',
    # E-Commerce themes
    'E-Commerce.themes.classic_gray',
    # E-Commerce
    'E-Commerce.core',
    'E-Commerce.admin',
    'E-Commerce.api',
    'E-Commerce.addons',
    'E-Commerce.default_tax',
    'E-Commerce.front',
    'E-Commerce.front.apps.auth',
    'E-Commerce.front.apps.carousel',
    'E-Commerce.front.apps.customer_information',
    'E-Commerce.front.apps.personal_order_history',
    'E-Commerce.front.apps.saved_carts',
    'E-Commerce.front.apps.registration',
    'E-Commerce.front.apps.simple_order_notification',
    'E-Commerce.front.apps.simple_search',
    'E-Commerce.front.apps.recently_viewed_products',
    'E-Commerce.notify',
    'E-Commerce.simple_cms',
    'E-Commerce.customer_group_pricing',
    'E-Commerce.campaigns',
    'E-Commerce.simple_supplier',
    'E-Commerce.order_printouts',
    'E-Commerce.utils',
    'E-Commerce.xtheme',
    'E-Commerce.reports',
    'E-Commerce.default_reports',
    'E-Commerce.regions',
    'E-Commerce.importer',
    'E-Commerce.default_importer',
    'E-Commerce.gdpr',
    'E-Commerce.tasks',
    'E-Commerce.discounts',

    # external apps
    'bootstrap3',
    'django_countries',
    'django_jinja',
    'django_filters',
    'filer',
    'reversion',
    'registration',
    'rest_framework',
    'rest_framework_swagger'
])

MIDDLEWARE_CLASSES = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'E-Commerce.front.middleware.ProblemMiddleware',
    'E-Commerce.core.middleware.E-CommerceMiddleware',
    'E-Commerce.front.middleware.E-CommerceFrontMiddleware',
    'E-Commerce.xtheme.middleware.XthemeMiddleware',
    'E-Commerce.admin.middleware.E-CommerceAdminMiddleware'
]

ROOT_URLCONF = 'E-Commerce_workbench.urls'
WSGI_APPLICATION = 'E-Commerce_workbench.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

LANGUAGE_CODE = 'en'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
STATIC_URL = '/static/'
LOGIN_REDIRECT_URL = '/'
SOUTH_TESTS_MIGRATE = False  # Makes tests that much faster.
DEFAULT_FROM_EMAIL = 'no-reply@example.com'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

LOGGING = {
    'version': 1,
    'formatters': {
        'verbose': {'format': '[%(asctime)s] (%(name)s:%(levelname)s): %(message)s'},
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'E-Commerce': {'handlers': ['console'], 'level': 'DEBUG', 'propagate': True},
    }
}

LANGUAGES = [
    # List all supported languages here.
    #
    # Should be a subset of django.conf.global_settings.LANGUAGES.  Use
    # same spelling for the language names for utilizing the language
    # name translations from Django.
    ('en', 'English'),
    ('fi', 'Finnish'),
    ('it', 'Italian'),
    ('ja', 'Japanese'),
    ('pt-br', 'Brazilian Portuguese'),
    ('ru', 'Russian'),
    ('sv', 'Swedish'),
    ('zh-hans', 'Simplified Chinese'),
]

PARLER_DEFAULT_LANGUAGE_CODE = "en"

PARLER_LANGUAGES = {
    None: [{"code": c, "name": n} for (c, n) in LANGUAGES],
    'default': {
        'hide_untranslated': False,
    }
}

_TEMPLATE_CONTEXT_PROCESSORS = [
    "django.contrib.auth.context_processors.auth",
    "django.template.context_processors.debug",
    "django.template.context_processors.i18n",
    "django.template.context_processors.media",
    "django.template.context_processors.static",
    "django.template.context_processors.request",
    "django.template.context_processors.tz",
    "django.contrib.messages.context_processors.messages"
]

TEMPLATES = [
    {
        "BACKEND": "django_jinja.backend.Jinja2",
        "APP_DIRS": True,
        "OPTIONS": {
            "match_extension": ".jinja",
            "context_processors": _TEMPLATE_CONTEXT_PROCESSORS,
            "newstyle_gettext": True,
            "environment": "E-Commerce.xtheme.engine.XthemeEnvironment",
        },
        "NAME": "jinja2",
    },
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": _TEMPLATE_CONTEXT_PROCESSORS,
            "debug": DEBUG
        }
    },
]

# set login url here because of `login_required` decorators
LOGIN_URL = "/login/"

SESSION_SERIALIZER = "django.contrib.sessions.serializers.PickleSerializer"

E-Commerce_PRICING_MODULE = "customer_group_pricing"

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'E-Commerce.api.permissions.E-CommerceAPIPermission',
    )
}

JWT_AUTH = {
    'JWT_ALLOW_REFRESH': True
}

SWAGGER_SETTINGS = {
    "SUPPORTED_SUBMIT_METHODS": [
        "get"
    ]
}

# extend the submit methods only if DEBUG is True
if DEBUG:
    SWAGGER_SETTINGS["SUPPORTED_SUBMIT_METHODS"].extend(["post", "patch", "delete", "put"])

E-Commerce_SETUP_WIZARD_PANE_SPEC = [
    "E-Commerce.admin.modules.shops.views:ShopWizardPane",
    "E-Commerce.admin.modules.service_providers.views.PaymentWizardPane",
    "E-Commerce.admin.modules.service_providers.views.CarrierWizardPane",
    "E-Commerce.xtheme.admin_module.views.ThemeWizardPane",
    "E-Commerce.testing.modules.sample_data.views.SampleObjectsWizardPane" if DEBUG else "",
    "E-Commerce.admin.modules.system.views.TelemetryWizardPane"
]


E-Commerce_ERROR_PAGE_HANDLERS_SPEC = [
    "E-Commerce.admin.error_handlers:AdminPageErrorHandler",
    "E-Commerce.front.error_handlers:FrontPageErrorHandler"
]

E-Commerce_SIMPLE_SEARCH_LIMIT = 150

if os.environ.get("E-Commerce_WORKBENCH_DISABLE_MIGRATIONS") == "1":
    from .utils import get_disabled_migrations
    MIGRATION_MODULES = get_disabled_migrations()


def configure(setup):
    setup.commit(globals())
