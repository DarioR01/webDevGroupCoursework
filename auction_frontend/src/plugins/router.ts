import { createRouter, createWebHistory } from 'vue-router';

const routes = [
    {path: '', name: 'Home', component: () => import('../Pages/HomePage/index.vue')},
    {path: '/profile', name: 'Profile', component: () => import('../Pages/ProfilePage/index.vue')},
];

const router = createRouter({routes, history: createWebHistory()});

export default router;