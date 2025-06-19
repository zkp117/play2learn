const game = process.env.VUE_APP_GAME;

module.exports = {
  publicPath: `/vue-games/${game}/`,  // for correct relative paths
  outputDir: 'dist',
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
