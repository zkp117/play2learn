import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import axios from 'axios';
import VueAxios from 'vue-axios';

// Axios settings
axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFTOKEN';
axios.defaults.withCredentials = true;

// Create app but DO NOT MOUNT
const app = createApp(App);
app.use(router);
app.use(VueAxios, axios);

// Export the app to global so Django template can mount it
window.vueApp = app;

