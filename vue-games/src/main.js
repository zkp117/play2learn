import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import axios from 'axios';
import VueAxios from 'vue-axios';

// Axios config
axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFTOKEN';
axios.defaults.withCredentials = true;

// Create and export app to global scope
const app = createApp(App);
app.use(router);
app.use(VueAxios, axios);

// Expose it globally BEFORE mounting
window.vueApp = app;
