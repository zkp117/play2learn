import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  base: '/vue-games/anagram-hunt/',
  plugins: [vue()],
})
