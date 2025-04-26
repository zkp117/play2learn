// const { defineConfig } = require('@vue/cli-service')
// module.exports = defineConfig({
//   transpileDependencies: true
// })
// vue-games/vue.config.js
module.exports = {
  publicPath: '/static/vue-games/',
  outputDir: '../static/vue-games/',
  indexPath: '../../templates/vue-games/index.html',

  pages: {
    mathfacts: {
      entry: 'src/main.js',      // << Your entry point!
      template: 'public/index.html',
      filename: 'index.html'     // this still maps to templates/vue-games/index.html
    }
  },

  configureWebpack: {
    devServer: {
      devMiddleware: {
        writeToDisk: true
      }
    }
  }
};
