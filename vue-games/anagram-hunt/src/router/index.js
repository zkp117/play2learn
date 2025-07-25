import { createRouter, createWebHistory } from 'vue-router'
import AnagramHunt from '../apps/AnagramHunt.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: AnagramHunt,
    },
  ],
})

export default router
