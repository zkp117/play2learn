import { createRouter, createWebHistory } from 'vue-router';
import AnagramHunt from './apps/AnagramHunt.vue';
import MathFacts from './apps/MathFacts.vue';

const routes = [
  { path: '/vue-games/anagram-hunt', component: AnagramHunt },
  { path: '/vue-games/math-facts', component: MathFacts },
  // Add any other game routes here
];

const router = createRouter({
  history: createWebHistory(),  // Use the history mode
  routes,
});

export default router;
