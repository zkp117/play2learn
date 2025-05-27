module.exports = {
  publicPath: '/games/',
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
