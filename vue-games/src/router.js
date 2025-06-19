import { createRouter, createWebHistory } from 'vue-router'

import AnagramHunt from './apps/AnagramHunt.vue'
import MathFacts from './apps/MathFacts.vue'

// Base URL for router history — set via env or default to your Vue games folder
const base = process.env.VUE_APP_BASE_URL || '/vue-games/'

const routes = [
  // Redirect root path to math-facts (or change to your preferred default)
  { path: '/', redirect: '/math-facts' },

  { 
    path: '/anagram-hunt', 
    name: 'AnagramHunt', 
    component: AnagramHunt, 
    meta: { requiresAuth: true } 
  },

  { 
    path: '/math-facts', 
    name: 'MathFacts', 
    component: MathFacts, 
    meta: { requiresAuth: true } 
  },
]

const router = createRouter({
  history: createWebHistory(base),
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
