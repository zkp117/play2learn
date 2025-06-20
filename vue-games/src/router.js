import { createRouter, createWebHashHistory } from 'vue-router' // ← changed

import AnagramHunt from './apps/AnagramHunt.vue'
import MathFacts from './apps/MathFacts.vue'

const routes = [
  { path: '/vue-games/anagram-hunt', name: 'AnagramHunt', component: AnagramHunt, meta: { requiresAuth: true } },
  { path: '/vue-games/math-facts', name: 'MathFacts', component: MathFacts, meta: { requiresAuth: true } },
]

const router = createRouter({
  history: createWebHashHistory(), // ← changed
  routes,
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    const loggedIn = document.cookie.includes('sessionid')
    if (!loggedIn) {
      window.location.href = '/accounts/login/?next=' + encodeURIComponent(to.fullPath)
      return
    }
  }
  next()
})

export default router
