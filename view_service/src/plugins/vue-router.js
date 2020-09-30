import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
  {
    path: '',
    name: 'analyze',
    props: false,
    component: () => import('@/views/AnalysisView'),
    meta: {
      title: 'MLog | Analysis'
    }
  }
]

const router = new VueRouter({
  mode: 'history',
  routes: routes,
  scrollBehavior (to, from, savedPosition) {
    return { x: 0, y: 0 }
  }
})

export default router
