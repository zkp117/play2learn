import { createRouter, createWebHistory } from 'vue-router';
import AnagramHunt from './apps/AnagramHunt.vue';
import MathFacts from './apps/MathFacts.vue';

const routes = [
  { path: '/anagram-hunt', component: AnagramHunt, meta: { requiresAuth: true } },
  { path: '/math-facts', component: MathFacts, meta: { requiresAuth: true } },
];

const router = createRouter({
  history: createWebHistory('/vue-games/'),  // Important: base path matches Django URL prefix
  routes,
});

router.beforeEach((to, from, next) => {
  const loggedIn = document.cookie.includes('sessionid');

  if (to.matched.some(record => record.meta.requiresAuth) && !loggedIn) {
    window.location.href = '/accounts/login/?next=' + encodeURIComponent(to.fullPath);
    return;
  }
  next();
});

export default router;
