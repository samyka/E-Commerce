# This file is part of E-Commerce.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from .detail import LoginAsUserView, UserDetailView
from .list import UserListView
from .password import UserChangePasswordView, UserResetPasswordView
from .permissions import UserChangePermissionsView

__all__ = [
    "UserListView",
    "UserDetailView",
    "UserChangePasswordView",
    "UserResetPasswordView",
    "UserChangePermissionsView",
    "LoginAsUserView"
]
