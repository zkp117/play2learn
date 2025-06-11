import { createRouter, createWebHistory } from 'vue-router';
import AnagramHunt from './apps/AnagramHunt.vue';
import MathFacts from './apps/MathFacts.vue';

// Mock a function to check if user is logged in (replace with your real check)
function isLoggedIn() {
  // e.g. check a cookie, localStorage token, or make an API call
  return !!localStorage.getItem('user_token'); 
}

const routes = [
  { path: '/vue-games/anagram-hunt', component: AnagramHunt, meta: { requiresAuth: true } },
  { path: '/vue-games/math-facts', component: MathFacts, meta: { requiresAuth: true } },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

// Navigation guard to check login
router.beforeEach((to, from, next) => {
  if (to.meta.requiresAuth && !isLoggedIn()) {
    next({ path: '/login', query: { next: to.fullPath } }); // redirect to login page
  } else {
    next();
  }
});

export default router;
