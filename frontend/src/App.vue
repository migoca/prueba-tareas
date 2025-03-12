<template>
  <v-app>
    <v-app-bar
      app
      color="primary"
      dark
    >
      <div class="d-flex align-center">
        <v-img
          alt="Vuetify Logo"
          class="shrink mr-2"
          contain
          src="https://cdn.vuetifyjs.com/images/logos/vuetify-logo-dark.png"
          transition="scale-transition"
          width="40"
        />

        
      </div>

      <v-spacer></v-spacer>
    </v-app-bar>

    <v-main>
      <v-col>

        <v-row justify="center">
        <router-link to="/" class="pa-2">Home</router-link > <span class="pa-2">|</span>
        <router-link to="/familias" class="pa-2">Familias</router-link><span class="pa-2">|</span> 
        <router-link to="/tareas" class="pa-2">Tareas</router-link>
        </v-row>
      </v-col>

      <router-view/>

    </v-main>
  </v-app>
</template>

<script>

export default {
  name: 'App',

  data: () => ({
    //
  }),
};
</script>
<style>
a.router-link-exact-active {
  color: #42b983;
}
</style>
