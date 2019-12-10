# This file is part of E-Commerce.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
"""
WSGI config for E-Commerce_workbench project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application  # noqa (E402)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "E-Commerce_workbench.settings")  # noqa

application = get_wsgi_application()
