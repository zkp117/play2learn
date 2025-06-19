import { createApp } from 'vue';
import App from './App.vue';
import router from './router.js'; // adjust if router filename differs

const app = createApp(App);
app.use(router);

// Expose app globally for manual mounting in Django template
window.vueApp = app;

// DO NOT mount here — mounting happens in template manually
