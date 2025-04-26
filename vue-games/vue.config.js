module.exports = {
  publicPath: process.env.NODE_ENV === 'production' ? '/vue-games/' : '/',
  pages: {
    mathFacts: {
      entry: 'src/apps/math-facts/main.js',
      template: 'public/index.html',
      filename: 'math-facts/index.html',
    },
    anagramHunt: {
      entry: 'src/apps/anagram-hunt/main.js',
      template: 'public/index.html',
      filename: 'anagram-hunt/index.html',
    },
  },
};
