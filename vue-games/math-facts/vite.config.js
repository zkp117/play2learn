import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  base: '/vue-games/math-facts/',
  plugins: [vue()],
  build: {
    outDir: 'dist',
    manifest: true, 
    rollupOptions: {
      input: './src/main.js',
      output: {
        entryFileNames: 'js/[name].[hash].js',
        chunkFileNames: 'js/[name].[hash].js',
        assetFileNames: 'assets/[name].[hash][extname]'
      }
    }
  }
})
