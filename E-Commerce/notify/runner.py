# -- encoding: UTF-8 --
# This file is part of E-Commerce.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from __future__ import unicode_literals

import logging

from django.conf import settings

from .models import Script
from .script import Context

LOG = logging.getLogger(__name__)


def run_event(event, shop):
    """Run the event
    :param E-Commerce.notify.Event event: the event
    :param E-Commerce.Shop shop: the shop to run the event
    """

    # TODO: Add possible asynchronous implementation.
    for script in Script.objects.filter(event_identifier=event.identifier, enabled=True, shop=shop):
        try:
            script.execute(context=Context.from_event(event, shop))
        except Exception:  # pragma: no cover
            if settings.DEBUG:
                raise
            LOG.exception("Script %r failed for event %r" % (script, event))
