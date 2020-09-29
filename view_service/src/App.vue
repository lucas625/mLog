<template>
  <v-app id="app">
    <v-main>
      <router-view :key="$route.fullPath" />
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: 'App'
}
</script>
