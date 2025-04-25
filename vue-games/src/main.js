import { createApp } from 'vue';
import axios from 'axios';
import VueAxios from 'vue-axios';
import router from './router';
import App from './App.vue';

// CSRF setup for Django
axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFTOKEN';

const root = document.getElementById('math-game-root') || document.getElementById('app');
if (root) {
  const writeReviewUrl = root.dataset.writeReviewUrl; // optional
  const app = createApp(App);

  // Inject the review URL globally if needed
  if (writeReviewUrl) app.provide('writeReviewUrl', writeReviewUrl);

  app.use(router);
  app.use(VueAxios, axios);
  app.mount(root);
}

