import { createRouter, createWebHistory } from 'vue-router';

const routes = [
    {path: '', name: 'Home', component: () => import('../Pages/HomePage/index.vue')},
    {path: '/profile', name: 'Profile', component: () => import('../Pages/ProfilePage/index.vue')},
    {path: '/item/:id', name: 'Item', component: () => import('../Pages/ItemPage/index.vue')},
    {path: '/login', name: 'Login', component: () => import('../Pages/LoginPage/index.vue')},
    {path: '/registration', name: 'Registration', component: () => import('../Pages/RegistrationPage/index.vue')},
    
];

const router = createRouter({routes, history: createWebHistory()});

export default router;