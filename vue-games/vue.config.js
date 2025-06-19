module.exports = {
  publicPath: process.env.VUE_APP_BASE_URL || '/',
  outputDir: `dist/${process.env.VUE_APP_GAME || 'default'}`,
  filenameHashing: false,
  productionSourceMap: false,
  assetsDir: '',
};
