// const { defineConfig } = require('@vue/cli-service')
// module.exports = defineConfig({
//   transpileDependencies: true
// })
// vue-games/vue.config.js
module.exports = {
  // Set the base path for the built files
  publicPath: '/static/vue-games/',  // Ensure that the compiled assets are placed correctly when referenced

  // Define where the build output should be placed
  outputDir: '../static/vue-games/',  // This ensures build files go into static/vue-games

  // Optional: Customize the index.html output location (if you want it placed in templates folder)
  indexPath: '../../templates/vue-games/index.html', // This ensures the index.html file is placed in your templates directory

  configureWebpack: {
    devServer: {
      devMiddleware: {
        writeToDisk: true  // Ensures that the build files are written to disk during development
      }
    }
  }
};

