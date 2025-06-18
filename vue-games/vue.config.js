module.exports = {
  publicPath: '/vue-games/',
  outputDir: 'dist',
  indexPath: 'index.html',
  filenameHashing: false,
  productionSourceMap: false,

  css: {
    extract: true  // <-- explicitly extract CSS to separate files
  },

  configureWebpack: {
    devServer: {
      devMiddleware: {
        writeToDisk: true
      }
    }
  }
};
