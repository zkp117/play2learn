module.exports = {
  publicPath: '/', // Or use '/vue-games/' if deploying in a subdirectory
  outputDir: 'dist', // Direct output to the 'dist' folder within vue-games
  // Remove or adjust indexPath to avoid generating _base_vue.html
  indexPath: '../templates/index.html', // or adjust this path as needed

  configureWebpack: {
    devServer: {
      devMiddleware: {
        writeToDisk: true
      }
    }
  }
};
