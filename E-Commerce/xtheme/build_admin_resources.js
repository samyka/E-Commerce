/**
 * This file is part of E-Commerce.
 *
 * Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
 *
 * This source code is licensed under the OSL-3.0 license found in the
 * LICENSE file in the root directory of this source tree.
 */
const { getParcelBuildCommand, runBuildCommands } = require("E-Commerce-static-build-tools");

runBuildCommands([
    getParcelBuildCommand({
        cacheDir: "xtheme",
        outputDir: "static/xtheme/admin/",
        entryFile: "static_src/admin/xtheme_admin.less"
    }),
    getParcelBuildCommand({
        cacheDir: "xtheme",
        outputDir: "static/xtheme/admin",
        entryFile: "static_src/admin/script.js"
    }),
    getParcelBuildCommand({
        cacheDir: "xtheme",
        outputDir: "static/xtheme/admin/",
        entryFile: "static_src/admin/snippet.js"
    }),
    getParcelBuildCommand({
        cacheDir: "xtheme",
        outputDir: "static/xtheme/admin/",
        entryFile: "static_src/admin/snippet.less"
    })
]);
