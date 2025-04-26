module.exports = {
  publicPath: '/static/vue-games/math-facts/',  // This is where assets will be served from
  outputDir: 'dist/vue-games/math-facts/',     // This ensures the build files go here

  configureWebpack: {
    devServer: {
      devMiddleware: {
        writeToDisk: true  // This ensures that the build files are written to disk
      }
    }
  }
};
