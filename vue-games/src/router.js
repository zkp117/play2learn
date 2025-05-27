import { createRouter, createWebHistory } from 'vue-router';
import AnagramHunt from './apps/AnagramHunt.vue';
import MathFacts from './apps/MathFacts.vue';

// routes for the vue games
const routes = [
  { path: '/vue-games/anagram-hunt', component: AnagramHunt },
  { path: '/vue-games/math-facts', component: MathFacts },

];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
