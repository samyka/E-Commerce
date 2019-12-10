# -*- coding: utf-8 -*-
# This file is part of E-Commerce.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.

from django.forms.models import ModelForm
from filer.fields.file import AdminFileWidget

from E-Commerce.admin.forms.widgets import FileDnDUploaderWidget
from E-Commerce.utils.multilanguage_model_form import MultiLanguageModelForm


class E-CommerceAdminForm(MultiLanguageModelForm):

    def __init__(self, **kwargs):
        super(E-CommerceAdminForm, self).__init__(**kwargs)
        for field in self.fields:
            if issubclass(self.fields[field].widget.__class__, AdminFileWidget):
                self.fields[field].widget = FileDnDUploaderWidget(
                    upload_path="/default", kind="images", clearable=True)


class E-CommerceAdminFormNoTranslation(ModelForm):
    def __init__(self, **kwargs):
        super(E-CommerceAdminFormNoTranslation, self).__init__(**kwargs)
        for field in self.fields:
            if issubclass(self.fields[field].widget.__class__, AdminFileWidget):
                self.fields[field].widget = FileDnDUploaderWidget(
                    upload_path="/default", kind="images", clearable=True)
