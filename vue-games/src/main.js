// src/main.js or wherever your entry point is
import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import axios from 'axios';
import VueAxios from 'vue-axios';

// Configure Axios
axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFTOKEN';
axios.defaults.withCredentials = true;

// Directly create and mount the Vue app
createApp(App)
  .use(router)
  .use(VueAxios, axios)
  .mount('#app');
