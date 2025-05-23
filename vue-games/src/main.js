import { createApp } from 'vue'; // Vue 3 syntax
import App from './App.vue';
import router from './router';  // Import the router
import axios from 'axios';
import VueAxios from 'vue-axios';

// Set default Django cookies and headers
axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.withCredentials = true;

fetch("/api/check-auth/")
  .then(response => {
    if (!response.ok) {
      window.location.href = "/accounts/login/";
    }
  });

const app = createApp(App);

app.use(router); 
app.use(VueAxios, axios);

app.mount('#app');