/**
 * This file is part of E-Commerce.
 *
 * Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
 *
 * This source code is licensed under the OSL-3.0 license found in the
 * LICENSE file in the root directory of this source tree.
 */
import m from "mithril";

export function post(data) {
    return m.request({
        method: "POST",
        url: location.pathname,
        data: data,
        config: function(xhr) {
            xhr.setRequestHeader("X-CSRFToken", window.E-CommerceAdminConfig.csrf);
        }
    });
}

export function get(data) {
    return m.request({
        method: "GET",
        url: location.pathname,
        data: data
    });
}

export function handleResponseMessages(response) {
    const Messages = window.Messages;
    if (!Messages) {  // Messages module not available for whichever reason
        return;
    }
    const message = response.message;
    const error = response.error;
    if (error) {
        Messages.enqueue({tags: "error", text: error});
    }
    if (message) {
        Messages.enqueue({tags: "info", text: message});
    }
}
