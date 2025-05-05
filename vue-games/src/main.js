import { createApp } from 'vue'; // Vue 3 syntax
import App from './App.vue';
import router from './router';  // Import the router
import axios from 'axios';
import VueAxios from 'vue-axios';

// Set default Django cookies and headers
axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.withCredentials = true;

const app = createApp(App); // Create app instance

app.use(router); // Use the router
app.use(VueAxios, axios); // Use axios

app.mount('#app'); // Mount the app to the DOM
