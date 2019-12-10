# -*- coding: utf-8 -*-
# This file is part of E-Commerce.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from django.db.transaction import atomic


def create_task(shop, creator, task_type, task_name, comment=None, **kwargs):
    from E-Commerce.tasks.models import Task

    with atomic():
        task = Task(creator=creator, shop=shop, type=task_type, name=task_name, **kwargs)
        task.full_clean()
        task.save()
        if comment:
            task.comment(creator, comment)
        return task
