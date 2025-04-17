import { createWebHashHistory, createRouter } from "vue-router";

import AnagramHunt from "./apps/AnagramHunt";
import MathFacts from "./apps/MathFacts";

const routes = [
  {
    path: '/anagram-hunt',
    component: AnagramHunt
  },
  {
    path: '/math-facts',
    component: MathFacts
  },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes: routes,
});

export default router;