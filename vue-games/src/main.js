import { createApp } from 'vue';
import App from './App.vue';
import router from './router'; 
import axios from 'axios';
import VueAxios from 'vue-axios';

axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.withCredentials = true;

const app = createApp(App);

app.use(router); 
app.use(VueAxios, axios);

app.mount('#app');