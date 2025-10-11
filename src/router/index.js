import { createRouter, createWebHistory } from "vue-router";
import HomeView from '../views/HomeView.vue'
import PrivacidadView from "@/views/PrivacidadView.vue";
const routes = [
    {
      path: "/",
      name: "home",
      component: HomeView,
    },
    {
      path: "/aviso-de-privacidad",
      name: "aviso-de-privacidad",
      component: PrivacidadView,
    },
  ]
const router = createRouter({
  // history: createWebHistory(import.meta.env.BASE_URL),
  history: createWebHistory('#'),
  routes,
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition
    }
    if (to.hash) {
      return {
        el: to.hash,
        behavior: 'smooth'
      }
    }
    return { top: 0, behavior: 'smooth' }
  }

});

export default router;
