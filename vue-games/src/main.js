import { createApp } from 'vue';
import axios from 'axios';
import VueAxios from 'vue-axios';
import router from './router';
import App from './App.vue'; // <- make sure this is your main App wrapper

// CSRF setup for Django
axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFTOKEN';

const app = createApp(App);

app.use(router);
app.use(VueAxios, axios);

app.mount('#app');
