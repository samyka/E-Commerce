# -*- coding: utf-8 -*-
# This file is part of E-Commerce.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from E-Commerce import configuration


def is_tour_complete(shop, tour_key, user=None):
    """
    Check if the tour is complete

    :param tour_key: The tour key.
    :type field: str
    :return: whether tour is complete
    :rtype: Boolean
    """
    user_id = user.pk if user else "-"
    return configuration.get(shop, "E-Commerce_%s_%s_tour_complete" % (tour_key, user_id), False)


def set_tour_complete(shop, tour_key, complete=True, user=None):
    user_id = user.pk if user else "-"
    return configuration.set(shop, "E-Commerce_%s_%s_tour_complete" % (tour_key, user_id), complete)
