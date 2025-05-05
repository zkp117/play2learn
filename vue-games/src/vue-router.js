import Vue from 'vue';
import Router from 'vue-router';

// Import your game components
import AnagramHuntComponent from './components/AnagramHuntComponent';
import MathFactsComponent from './components/MathFactsComponent';

Vue.use(Router);

const routes = [
  { path: '/games/anagram-hunt', component: AnagramHuntComponent },
  { path: '/games/math-facts', component: MathFactsComponent },
];

const router = new Router({
  routes,
  mode: 'history',  // This ensures that URLs don't have a hash (#) in them
});

export default router;
