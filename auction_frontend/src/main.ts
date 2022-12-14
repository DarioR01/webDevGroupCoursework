import { createApp } from 'vue';
import App from './App.vue';
import router from './plugins/router.js';

import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';

import 'bootstrap/dist/js/bootstrap.js'
import 'bootstrap-vue/dist/bootstrap-vue.js';

createApp(App).use(router).mount('#app');
