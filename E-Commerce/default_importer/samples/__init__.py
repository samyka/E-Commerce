# This file is part of E-Commerce.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
import os


def get_sample_file_content(file_name):
    path = os.path.join(os.path.dirname(__file__), file_name)
    if os.path.exists(path):
        from six import BytesIO
        return BytesIO(open(path, "rb").read())
