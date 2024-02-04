// router/index.js
import { createRouter, createWebHistory } from 'vue-router';
import HomePage from './Home.vue';
import ResultPage from './Result.vue';
import ClassPage from './Class.vue';
import DatabasePage from './Database.vue';
import ViewQuestions from './ViewQuestions.vue';

const routes = [
  {
    path: '/',
    name: 'Home',
    component: HomePage,
  },
  {
    path: '/result',
    name: 'Result',
    component: ResultPage,
  },
  {
    path: '/class',
    name: 'Class',
    component: ClassPage,
  },
  {
    path: '/view-questions', // Use a dynamic segment for the user name
    name: 'ViewQuestions',
    component: ViewQuestions,
  },
  {
    path: '/database',
    name: 'Database',
    component: DatabasePage,
  }
];

const base = import.meta.env.BASE_URL || '/';

const router = createRouter({
  history: createWebHistory(base),
  routes,
});

export default router;
