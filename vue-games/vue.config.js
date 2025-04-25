// const { defineConfig } = require('@vue/cli-service')
// module.exports = defineConfig({
//   transpileDependencies: true
// })
module.exports = {
  // This will set the base URL for the assets. 
  // You can modify this depending on your production deployment URL.
  publicPath: '/vue-games/',  // Base URL for both games

  // You can specify different output directories for each game.
  // Ensure they are placed in separate subdirectories under 'vue-games'
  pages: {
    mathFacts: {
      entry: 'src/main.js',  // Adjust if your entry file is different
      outputDir: '../static/vue-games/math-facts/js',  // Path for math-facts build
      indexPath: '../../templates/_base_vue.html',  // Path for HTML file (you can adjust this as needed)
    },
    anagramHunt: {
      entry: 'src/main.js',  // Adjust if your entry file is different
      outputDir: '../static/vue-games/anagramhunt/js',  // Path for anagramhunt build
      indexPath: '../../templates/_base_vue.html',  // Path for HTML file (you can adjust this as needed)
    }
  },

  configureWebpack: {
    devServer: {
      devMiddleware: {
        writeToDisk: true  // Ensures that the build files are written to disk during development
      }
    }
  }
};

