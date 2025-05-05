module.exports = {
  // Dynamically set publicPath based on the VUE_APP_GAME environment variable
  publicPath: process.env.VUE_APP_GAME ? `/vue-games/${process.env.VUE_APP_GAME}/` : '/', 

  outputDir: 'dist',  // Keep the same output directory structure for simplicity
  indexPath: 'templates/index.html',  // Place the index.html in the templates folder
  filenameHashing: false,  // Disable filename hashing for simpler file names
  productionSourceMap: false,  // Disable source maps for production build

  configureWebpack: {
    devServer: {
      devMiddleware: {
        writeToDisk: true  // Ensure assets are written to disk
      }
    }
  }
};

