/**
 * This file is part of E-Commerce.
 *
 * Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
 *
 * This source code is licensed under the OSL-3.0 license found in the
 * LICENSE file in the root directory of this source tree.
 */
$(function() {
    $(".form-control.datetime").datetimepicker({
        format: window.E-CommerceAdminConfig.settings.datetimeInputFormat,
        step: window.E-CommerceAdminConfig.settings.datetimeInputStep
    });

    $(".form-control.date").datetimepicker({
        format: window.E-CommerceAdminConfig.settings.dateInputFormat,
        timepicker: false
    });

    $(".form-control.time").datetimepicker({
        format: window.E-CommerceAdminConfig.settings.timeInputFormat,
        datepicker: false,
        step: window.E-CommerceAdminConfig.settings.datetimeInputStep
    });

    jQuery.datetimepicker.setLocale(window.E-CommerceAdminConfig.settings.dateInputLocale);
});
