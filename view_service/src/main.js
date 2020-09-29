import Vue from 'vue'
import App from '@/App'
import router from '@/plugins/vue-router'
import vuetify from '@/plugins/vuetify'

Vue.config.productionTip = false
require('dotenv').config()

new Vue({
  router,
  vuetify,
  render: h => h(App)
}).$mount('#app')
