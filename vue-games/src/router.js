import { createRouter, createWebHistory } from 'vue-router'
import AnagramHunt from './apps/AnagramHunt.vue'
import MathFacts from './apps/MathFacts.vue'

const base = process.env.VUE_APP_BASE_URL || '/vue-games/'  // GOOD

const routes = [
  { path: 'math-facts', name: 'MathFacts', component: MathFacts, meta: { requiresAuth: true } },
  { path: 'anagram-hunt', name: 'AnagramHunt', component: AnagramHunt, meta: { requiresAuth: true } },
  { path: '', redirect: 'math-facts' }, // root inside base redirects relatively
];

const router = createRouter({
  history: createWebHistory(base),
  routes,
})

router.beforeEach((to, from, next) => {
  const loggedIn = document.cookie.includes('sessionid')
  if (to.meta.requiresAuth && !loggedIn) {
    window.location.href = `/accounts/login/?next=${encodeURIComponent(to.fullPath)}`
  } else {
    next()
  }
})

export default router
