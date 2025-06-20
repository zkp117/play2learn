import { createRouter, createWebHistory } from 'vue-router'
import MathFactsComponent from './MathFacts.vue'

const routes = [
  { path: '/', component: MathFactsComponent }
]

const router = createRouter({
  history: createWebHistory('/vue-games/math-facts/'),
  routes,
})

export default router
