import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import axios from 'axios';
import VueAxios from 'vue-axios';

// Axios config for CSRF
axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFTOKEN';
axios.defaults.withCredentials = true;

// Create and mount Vue app on #app (from _base_vue.html)
createApp(App)
  .use(router)
  .use(VueAxios, axios)
  .mount('#app');
