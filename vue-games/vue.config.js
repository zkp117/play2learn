// const { defineConfig } = require('@vue/cli-service')
// module.exports = defineConfig({
//   transpileDependencies: true
// })
module.exports = {
  filenameHashing: false,
  publicPath: 'https://play2learn-bucket.s3.amazonaws.com/static/',
  outputDir: '../static/dist',
  indexPath: '../../templates/_base_vue.html',
  configureWebpack: {
    devServer: {
      devMiddleware: {
        writeToDisk: true
      }
    }
  }
}
