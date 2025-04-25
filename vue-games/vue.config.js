// const { defineConfig } = require('@vue/cli-service')
// module.exports = defineConfig({
//   transpileDependencies: true
// })
module.exports = {
  publicPath: '/static/vue/',  // Base URL for assets
  outputDir: '../static/vue-games/math-facts/js',  // Ensure files are output in the correct path
  indexPath: '../../templates/_base_vue.html', // The path for the index file

  configureWebpack: {
    devServer: {
      devMiddleware: {
        writeToDisk: true
      }
    }
  }
};
