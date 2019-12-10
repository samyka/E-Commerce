# This file is part of E-Commerce.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
import json
import pytest

from E-Commerce.utils.models import get_data_dict
from E-Commerce.testing import factories


@pytest.mark.django_db
def test_get_data_dict_force_value_with_json_serializer():
    product = factories.get_default_product()

    with pytest.raises(TypeError):
        json.dumps(get_data_dict(product))

    json.dumps(get_data_dict(product, force_text_for_value=True))
