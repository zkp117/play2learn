import { createRouter, createWebHistory } from 'vue-router';
import AnagramHunt from './apps/AnagramHunt.vue';
import MathFacts from './apps/MathFacts.vue';

const routes = [
  { path: '/vue-games/anagram-hunt', component: AnagramHunt, meta: { requiresAuth: true } },
  { path: '/vue-games/math-facts', component: MathFacts, meta: { requiresAuth: true } },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

// Global navigation guard for authentication
router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    // Simple check for Django session cookie
    const loggedIn = document.cookie.includes('sessionid'); // adjust if your session cookie name is different

    if (!loggedIn) {
      // Redirect browser to Django login page with "next" param for redirect after login
      window.location.href = '/accounts/login/?next=' + encodeURIComponent(to.fullPath);
      return; // stop Vue navigation here
    }
  }
  next(); // continue normally if logged in or route doesn't require auth
});

export default router;
