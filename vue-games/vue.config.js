// vue.config.js
module.exports = {
  publicPath: 'https://play2learn-bucket.s3.amazonaws.com/vue-games/math-facts/',
  outputDir: 'dist/vue-games/math-facts/',

  configureWebpack: {
    devServer: {
      devMiddleware: {
        writeToDisk: true
      }
    }
  }
};
