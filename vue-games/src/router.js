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

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    const loggedIn = document.cookie.includes('sessionid');

    if (!loggedIn) {
      window.location.href = '/accounts/login/?next=' + encodeURIComponent(to.fullPath);
      return;
    }
  }
  next();
});

export default router;
