import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  base: '/vue-games/math-facts/',
  plugins: [vue()],
  build: {
    rollupOptions: {
      output: {
        entryFileNames: `js/app.js`,
        chunkFileNames: `js/chunk-vendors.js`,
        assetFileNames: `assets/[name][extname]`
      }
    }
  }
})
