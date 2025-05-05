import Vue from 'vue';
import Router from 'vue-router';

// Import your game components
import AnagramHunt from './apps/AnagramHunt';
import MathFacts from './apps/MathFacts.';

Vue.use(Router);  // Telling Vue to use Vue Router

const routes = [
  { path: '/vue-games/anagram-hunt', component: AnagramHunt },
  { path: '/vue-games/math-facts', component: MathFacts },
  // Add any other game routes here as needed
];

const router = new Router({
  routes, // Define the routes
  mode: 'history', // Use HTML5 History API (optional but cleaner)
});

export default router;
