import { createRouter, createWebHistory } from 'vue-router'
import AnagramHunt from './apps/AnagramHunt.vue'
import MathFacts from './apps/MathFacts.vue'
import axios from 'axios'

// Use base URL from env or default
const base = process.env.VUE_APP_BASE_URL || '/vue-games/'

const routes = [
  {
    path: '/math-facts',   // <-- add leading slash here
    name: 'MathFacts',
    component: MathFacts,
    meta: { requiresAuth: true },
  },
  {
    path: '/anagram-hunt',  // <-- add leading slash here
    name: 'AnagramHunt',
    component: AnagramHunt,
    meta: { requiresAuth: true },
  },
  {
    path: '/',
    redirect: '/math-facts',  // redirect to valid absolute path
  },
]

const router = createRouter({
  history: createWebHistory(base),
  routes,
})

// Axios CSRF & credentials setup (good)
axios.defaults.withCredentials = true
axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFTOKEN'

// Route guard to check login (looks good)
router.beforeEach(async (to, from, next) => {
  if (to.meta.requiresAuth) {
    try {
      const response = await axios.get('/api/is-logged-in/', {
        withCredentials: true,
      })

      if (response.data.logged_in) {
        next()
      } else {
        window.location.href = `/accounts/login/?next=${encodeURIComponent(to.fullPath)}`
      }
    } catch (error) {
      console.error('Auth check failed:', error)
      window.location.href = `/accounts/login/?next=${encodeURIComponent(to.fullPath)}`
    }
  } else {
    next()
  }
})

export default router
