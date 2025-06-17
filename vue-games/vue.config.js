module.exports = {
  publicPath: 'https://play2learn-bucket.s3.us-east-2.amazonaws.com/vue-games/',
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
