module.exports = {
  publicPath: '/static/vue-games/',
  outputDir: 'dist',
  indexPath: 'templates/index.html',
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
