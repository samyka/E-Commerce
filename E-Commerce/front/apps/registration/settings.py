# This file is part of E-Commerce.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
#: Require email-based activation for users?
#:
#: This corresponds to using the `default` or `simple`
#: `django-registration` backends.
E-Commerce_REGISTRATION_REQUIRES_ACTIVATION = True

#: The E-Commerce default registration form for person
#: This overrides the setting from `registration` lib
#: to allow custom logic like receiving the request from kwargs
REGISTRATION_FORM = "E-Commerce.front.apps.registration.forms.PersonRegistrationForm"
