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
        cacheDir: "classic_gray",
        outputDir: "static/E-Commerce/classic_gray/pink",
        entryFile: "static_src/pink/style.css"
    }),
    getParcelBuildCommand({
        cacheDir: "classic_gray",
        outputDir: "static/E-Commerce/classic_gray/blue",
        entryFile: "static_src/blue/style.css"
    })
]);
