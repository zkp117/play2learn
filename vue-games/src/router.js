import { createRouter, createWebHistory } from 'vue-router'
import MathFacts from './apps/MathFacts.vue'
import AnagramHunt from './apps/AnagramHunt.vue'

const routes = [
  {
    path: '/math-facts',
    name: 'MathFacts',
    component: MathFacts
  },
  {
    path: '/anagram-hunt',
    name: 'AnagramHunt',
    component: AnagramHunt
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
