module.exports = {
  publicPath: '/games/',  // Make sure it's just '/games/', not dynamic
  outputDir: 'dist',  // Output directory for production build
  indexPath: 'templates/index.html',  // Place index.html inside Django's templates directory
  filenameHashing: false,  // Disable filename hashing for cleaner filenames
  productionSourceMap: false,  // Disable source maps in production

  configureWebpack: {
    devServer: {
      devMiddleware: {
        writeToDisk: true  // Ensure assets are written to disk for Django to serve them
      }
    }
  }
};
