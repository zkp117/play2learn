import { createApp } from 'vue';
import App from './App.vue';  // The root component of the app
import router from './router.js';  // Import the router configuration

// Create the Vue app and mount it with the router
createApp(App)
  .use(router)  // Add the router to the app
  .mount('#app');  // Mount the app to the div with id "app"
