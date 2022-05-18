<template>
  <v-container class="lighten-5 pa-3" fluid>
    <v-row width="100%" no-gutters>
      <v-col cols="8" class="ml-auto">
        <v-card class="pa-2 ma-3" outlined> First, but last </v-card>
        <v-toolbar
          dense
          class="pa-2 ma-3"
          elevation="0"
          outlined
          rounded
        ></v-toolbar>
        <v-card class="pa-2 ma-3" outlined> First, but last </v-card>
      </v-col>
      <v-col cols="4">
        <v-card class="pa-2 ma-3" outlined> Second, but unordered </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: 'IndexPage',
}
</script>
