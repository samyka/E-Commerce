# -*- coding: utf-8 -*-
# This file is part of E-Commerce.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from E-Commerce.apps import AppConfig
from E-Commerce.apps.settings import validate_templates_configuration


class E-CommerceAdminAppConfig(AppConfig):
    name = "E-Commerce.admin"
    verbose_name = "E-Commerce Admin"
    label = "E-Commerce_admin"
    required_installed_apps = ["bootstrap3"]
    provides = {
        "admin_module": [
            "E-Commerce.admin.modules.system:SystemModule",
            "E-Commerce.admin.modules.products:ProductModule",
            "E-Commerce.admin.modules.product_types:ProductTypeModule",
            "E-Commerce.admin.modules.media:MediaModule",
            "E-Commerce.admin.modules.orders:OrderModule",
            "E-Commerce.admin.modules.orders:OrderStatusModule",
            "E-Commerce.admin.modules.taxes:TaxModule",
            "E-Commerce.admin.modules.categories:CategoryModule",
            "E-Commerce.admin.modules.contacts:ContactModule",
            "E-Commerce.admin.modules.contact_groups:ContactGroupModule",
            "E-Commerce.admin.modules.contact_group_price_display:ContactGroupPriceDisplayModule",
            "E-Commerce.admin.modules.currencies:CurrencyModule",
            "E-Commerce.admin.modules.customers_dashboard:CustomersDashboardModule",
            "E-Commerce.admin.modules.permission_groups:PermissionGroupModule",
            "E-Commerce.admin.modules.users:UserModule",
            "E-Commerce.admin.modules.service_providers:ServiceProviderModule",
            "E-Commerce.admin.modules.services:PaymentMethodModule",
            "E-Commerce.admin.modules.services:ShippingMethodModule",
            "E-Commerce.admin.modules.attributes:AttributeModule",
            "E-Commerce.admin.modules.sales_units:DisplayUnitModule",
            "E-Commerce.admin.modules.sales_units:SalesUnitModule",
            "E-Commerce.admin.modules.sales_dashboard:SalesDashboardModule",
            "E-Commerce.admin.modules.shops:ShopModule",

            "E-Commerce.admin.modules.manufacturers:ManufacturerModule",
            "E-Commerce.admin.modules.suppliers:SupplierModule",
            "E-Commerce.admin.modules.support:E-CommerceSupportModule",
            "E-Commerce.admin.modules.settings.SettingsModule",
            "E-Commerce.admin.modules.labels:LabelsModule",
            "E-Commerce.admin.modules.menu:AdminMenuModule",
        ],
        "admin_shop_form_part": [
            "E-Commerce.admin.modules.settings.form_parts.OrderConfigurationFormPart"
        ],
        "service_provider_admin_form": [
            "E-Commerce.admin.modules.service_providers.forms:CustomCarrierForm",
            "E-Commerce.admin.modules.service_providers.forms:CustomPaymentProcessorForm"
        ],
        "carrier_wizard_form_def": [
            "E-Commerce.admin.modules.service_providers.wizard_form_defs:ManualShippingWizardFormDef"
        ],
        "payment_processor_wizard_form_def": [
            "E-Commerce.admin.modules.service_providers.wizard_form_defs:ManualPaymentWizardFormDef"
        ],
        "service_behavior_component_form": [
            "E-Commerce.admin.modules.services.forms:FixedCostBehaviorComponentForm",
            "E-Commerce.admin.modules.services.forms:WaivingCostBehaviorComponentForm",
            "E-Commerce.admin.modules.services.forms:WeightLimitsBehaviorComponentForm",
            "E-Commerce.admin.modules.services.forms:GroupAvailabilityBehaviorComponentForm",
            "E-Commerce.admin.modules.services.forms.StaffOnlyBehaviorComponentForm",
            "E-Commerce.admin.modules.services.forms.OrderTotalLimitBehaviorComponentForm",
            "E-Commerce.admin.modules.services.forms.CountryLimitBehaviorComponentForm",
        ],
        "service_behavior_component_form_part": [
            "E-Commerce.admin.modules.services.weight_based_pricing.WeightBasedPricingFormPart"
        ],
        "admin_order_section": [
            "E-Commerce.admin.modules.orders.sections:BasicDetailsOrderSection",
            "E-Commerce.admin.modules.orders.sections:PaymentOrderSection",
            "E-Commerce.admin.modules.orders.sections:LogEntriesOrderSection",
            "E-Commerce.admin.modules.orders.sections:ShipmentSection",
            "E-Commerce.admin.modules.orders.sections:AdminCommentSection",
        ],
        "admin_contact_section": [
            "E-Commerce.admin.modules.contacts.sections:BasicInfoContactSection",
            "E-Commerce.admin.modules.contacts.sections:AddressesContactSection",
            "E-Commerce.admin.modules.contacts.sections:OrdersContactSection",
            "E-Commerce.admin.modules.contacts.sections:MembersContactSection",
        ],
        "admin_product_section": [
            "E-Commerce.admin.modules.products.sections:ProductOrdersSection"
        ],
        "admin_order_toolbar_action_item": [
            "E-Commerce.admin.modules.orders.toolbar:CreatePaymentAction",
            "E-Commerce.admin.modules.orders.toolbar:SetPaidAction",
            "E-Commerce.admin.modules.orders.toolbar:CreateRefundAction",
            "E-Commerce.admin.modules.orders.toolbar:EditAddresses",
        ],
        "admin_model_url_resolver": [
            "E-Commerce.admin.utils.urls.get_model_url"
        ],
        "admin_browser_config_provider": [
            "E-Commerce.admin.browser_config:DefaultBrowserConfigProvider"
        ]
    }

    def ready(self):
        from E-Commerce.core.order_creator.signals import order_creator_finished
        from E-Commerce.admin.modules.orders.receivers import handle_custom_payment_return_requests

        order_creator_finished.connect(handle_custom_payment_return_requests,
                                       dispatch_uid='E-Commerce.admin.handle_cash_payments')

        validate_templates_configuration()


default_app_config = "E-Commerce.admin.E-CommerceAdminAppConfig"
