import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  base: '/vue-games/math-facts/',  // or '/vue-games/anagram-hunt/' in the other config
  plugins: [vue()],
  build: {
    rollupOptions: {
      output: {
        entryFileNames: `js/app.js`,
        // remove chunkFileNames to avoid chunk-vendors.js
        // chunkFileNames: `js/chunk-vendors.js`, <-- remove/comment this
        assetFileNames: `assets/[name][extname]`
      }
    }
  }
})
