# -*- coding: utf-8 -*-
# This file is part of E-Commerce.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from django.core.urlresolvers import reverse_lazy

from E-Commerce.admin.form_part import FormPartsViewMixin, SaveFormPartsMixin
from E-Commerce.admin.modules.categories.form_parts import (
    CategoryBaseFormPart, CategoryProductFormPart
)
from E-Commerce.admin.shop_provider import get_shop
from E-Commerce.admin.toolbar import get_default_edit_toolbar
from E-Commerce.admin.utils.tour import is_tour_complete
from E-Commerce.admin.utils.views import CreateOrUpdateView
from E-Commerce.core.models import Category


class CategoryEditView(SaveFormPartsMixin, FormPartsViewMixin, CreateOrUpdateView):
    model = Category
    template_name = "E-Commerce/admin/categories/edit.jinja"
    context_object_name = "category"
    base_form_part_classes = [CategoryBaseFormPart, CategoryProductFormPart]
    form_part_class_provide_key = "admin_category_form_part"

    def get_toolbar(self):
        save_form_id = self.get_save_form_id()
        object = self.get_object()
        delete_url = reverse_lazy("E-Commerce_admin:category.delete", kwargs={"pk": object.pk}) if object.pk else None
        return get_default_edit_toolbar(self, save_form_id, delete_url=delete_url)

    def get_context_data(self, **kwargs):
        context = super(CategoryEditView, self).get_context_data(**kwargs)
        context["tour_key"] = "category"
        context["tour_complete"] = is_tour_complete(get_shop(self.request), "category", user=self.request.user)
        if self.object.pk:
            context["title"] = self.object.name

        return context

    def form_valid(self, form):
        return self.save_form_parts(form)

    def get_queryset(self):
        return Category.objects.all_except_deleted(shop=get_shop(self.request))
