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
        cacheDir: "front",
        outputDir: "static/E-Commerce/front/js",
        entryFile: "static_src/js/vendor.js"
    }),
    getParcelBuildCommand({
        cacheDir: "front",
        outputDir: "static/E-Commerce/front/js",
        outputFileName: "scripts",
        entryFile: "static_src/js/index.js"
    }),
    getParcelBuildCommand({
        cacheDir: "front",
        outputDir: "static/E-Commerce/front/css",
        entryFile: "static_src/less/style.css"
    })
]);
