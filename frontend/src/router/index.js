import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import useComment from "../views/useComment.vue";
import LoginView from '../views/LoginView.vue';
import SignUp from '../views/SignUp.vue';
import RatingComponent from "../views/RatingComponent.vue";

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/UpdateView',
    name: 'UpdateView',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/UpdateView.vue')
  },
  {
    path: "/useComment",
    name: "useComment",
    component: useComment,
  },
  {
    path: "/RatingComponent/:showId",
    name: "RatingComponent",
    component: RatingComponent,
  },
  {
    path: '/LoginView',
    name: 'LoginView',
    component: LoginView,
  },
  {
    path: '/SignUp',
    name: 'SignUp',
    component: SignUp,
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
