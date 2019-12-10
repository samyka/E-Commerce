/**
 * This file is part of E-Commerce.
 *
 * Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
 *
 * This source code is licensed under the OSL-3.0 license found in the
 * LICENSE file in the root directory of this source tree.
 */
const { getParcelBuildCommand, runBuildCommands } = require("E-Commerce-static-build-tools");

const srcFiles = [
  { entry: "static_src/base/scss/style.scss", name: "base"},
  { entry: "static_src/dashboard/scss/dashboard.scss"},
  { entry: "static_src/wizard/scss/wizard.scss"},
  { entry: "modules/media/static_src/media/browser/media-browser.scss"},
];

runBuildCommands(
  srcFiles.map(file => {
    return getParcelBuildCommand({
      cacheDir: "admin",
      entryFile: file.entry,
      outputFileName: (file.name !== 'undefined') ? file.name : null,
      outputDir: (file.entry.includes('.js')) ? "static/E-Commerce_admin/js" : "static/E-Commerce_admin/css"
    })
  })
);

