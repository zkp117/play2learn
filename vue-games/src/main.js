import { createApp } from 'vue';
import axios from 'axios';
import VueAxios from 'vue-axios';

import router from './router'; // import our router
import App from "./App";

// set default Django cookies and headers
axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";

const el = document.getElementById('math-game-root');
if (el){
  createApp(MathFacts).mount(el);
}
const app = createApp(App); // create our app instance

app.use(router); // tell our app to use our router

app.use(VueAxios, axios); // tell our app to use axios

app.mount("#app"); // mount our app on the div#app element in our template