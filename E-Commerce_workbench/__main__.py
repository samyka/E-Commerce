#!/usr/bin/env python
# This file is part of E-Commerce.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
import logging
import os
import sys
import warnings

from E-Commerce.utils.deprecation import RemovedInFutureE-CommerceWarning

if __name__ == "__main__":
    if not sys.warnoptions:
        # Route warnings through python logging
        logging.captureWarnings(True)
        # RemovedInFutureE-CommerceWarning is a subclass of PendingDeprecationWarning which
        # is hidden by default, hence we force the "default" behavior
        warnings.simplefilter("default", RemovedInFutureE-CommerceWarning)
    sys.path.insert(0, os.path.realpath(os.path.dirname(__file__) + "/.."))
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "E-Commerce_workbench.settings")
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
