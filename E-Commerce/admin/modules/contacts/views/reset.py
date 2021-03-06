# -*- coding: utf-8 -*-
# This file is part of E-Commerce.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from django.utils.translation import ugettext_lazy as _

from E-Commerce.admin.modules.contacts.utils import check_contact_permission
from E-Commerce.admin.modules.users.views.password import UserResetPasswordView
from E-Commerce.admin.utils.urls import get_model_url
from E-Commerce.core.models import Contact
from E-Commerce.utils.excs import Problem


class ContactResetPasswordView(UserResetPasswordView):
    def get_contact(self):
        contact = Contact.objects.get(pk=self.kwargs[self.pk_url_kwarg])
        check_contact_permission(self.request, contact)
        return contact

    def get_object(self, queryset=None):
        contact = self.get_contact()
        user = getattr(contact, "user", None)
        if not user:
            raise Problem(_(u"The contact does not have an associated user."))
        return user

    def get_success_url(self):
        return get_model_url(self.get_contact())
