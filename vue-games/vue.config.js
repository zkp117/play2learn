module.exports = {
  // This should be the **base URL path** your app is served from, relative to the domain
  publicPath: '/vue-games/',

  outputDir: 'dist',

  // Only set indexPath like this if you want Vue build to output the index.html into a specific folder
  // Usually you can leave this default, but if you want your Django templates to point to a static file, you can configure accordingly
  indexPath: 'index.html',

  filenameHashing: false,
  productionSourceMap: false,

  configureWebpack: {
    devServer: {
      devMiddleware: {
        writeToDisk: true
      }
    }
  }
};
