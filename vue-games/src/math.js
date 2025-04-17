import { createApp } from 'vue';
import MathFacts from './MathFacts.vue';
import router from './router';

createApp(MathFacts).mount('#math-facts');
app.use(router);
app.mount('#math-app');