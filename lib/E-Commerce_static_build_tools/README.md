E-Commerce Static Build Tools
------------------------

This lib provides utilities to build [E-Commerce](https://github.com/E-Commerce/E-Commerce) static sources using [Parcel Bundler](https://parceljs.org/).

## Installation

```shell
$ npm i --save E-Commerce-static-build-tools
```

## Usage

Create a Node.js script to build files, example `build_resources.js`:

```js
const { getParcelBuildCommand, runBuildCommands } = require("E-Commerce-static-build-tools");

runBuildCommands([
    getParcelBuildCommand({
        cacheDir: "myapp",
        outputDir: "static/myapp/",
        entryFile: "static_src/myapp.js"
    }),
    getParcelBuildCommand({
        cacheDir: "myapp",
        outputDir: "static/myapp/",
        entryFile: "static_src/myapp.less"
    })
]);
```

Add in your `packages.json`:

```json
"scripts": {
    "watch": "node build_resources --watch",
    "build": "node build_resources"
},
"E-Commerce": {
    "static_build": true
}
```

Now you can use E-Commerce static build tool to build your app alogn with all E-Commerce apps:

```
python setup.py build_resources
```

Note: make sure to follow [Parcel Bundler](https://parceljs.org/) steps to install all the required addsons for transforming your code correctly.

## License

OSL-3.0
