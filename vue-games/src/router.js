import { createRouter, createWebHistory } from 'vue-router'

const game = process.env.VUE_APP_GAME

let routes = []
let base = '/vue-games/'

if (game === 'math-facts') {
  const MathFacts = () => import('./apps/MathFacts.vue')
  routes = [
    {
      path: '/',
      name: 'MathFacts',
      component: MathFacts,
      meta: { requiresAuth: true },
    },
  ]
  base += 'math-facts/'
} else if (game === 'anagram-hunt') {
  const AnagramHunt = () => import('./apps/AnagramHunt.vue')
  routes = [
    {
      path: '/',
      name: 'AnagramHunt',
      component: AnagramHunt,
      meta: { requiresAuth: true },
    },
  ]
  base += 'anagram-hunt/'
} else {
  console.error('Unknown game:', game)
}

const router = createRouter({
  history: createWebHistory(base),
  routes,
})

router.beforeEach((to, from, next) => {
  const loggedIn = document.cookie.includes('sessionid')
  if (!loggedIn) {
    window.location.href = '/accounts/login/?next=' + encodeURIComponent(to.fullPath)
    return
  }
  next()
})

export default router