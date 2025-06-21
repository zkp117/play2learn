import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  base: '/vue-games/anagram-hunt/', // or math-facts/
  plugins: [vue()],
  build: {
    target: 'es2015',  // ✅ Ensures no raw "export" syntax in JS output
    rollupOptions: {
      output: {
        entryFileNames: `js/app.js`,
        chunkFileNames: `js/chunk-vendors.js`,
        assetFileNames: `assets/[name].[ext]`,
      }
    }
  }
})
