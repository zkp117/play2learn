import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import path from 'path'

export default defineConfig({
  base: '/vue-games/anagram-hunt/',
  plugins: [vue()],
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src')
    }
  },
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
