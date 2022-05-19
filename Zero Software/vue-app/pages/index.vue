<script>
import Pallette from '../components/pallette.vue'
import OptionsList from '../components/options-list.vue'
import PixelConfiguration from '../components/pixel-configuration.vue'

export default {
  name: 'IndexPage',
  components: {
    Pallette,
    OptionsList,
    PixelConfiguration,
  },
  computed: {
    optionsListVisible() {
      console.log(this)
      switch (this.$vuetify.breakpoint.name) {
        case 'xs':
          return false
        case 'sm':
          return false
        default:
          return true
      }
    },
  },
}
</script>

<template>
  <v-container class="lighten-5 pa-3" fluid>
    <v-row width="100%" no-gutters>
      <v-col :cols="optionsListVisible ? 8 : 12" class="ml-auto">
        <Pallette />
        <v-toolbar
          dense
          class="pa-2 ma-3"
          elevation="0"
          outlined
          rounded
        ></v-toolbar>
        <PixelConfiguration />
      </v-col>
      <v-col cols="4" v-if="optionsListVisible">
        <OptionsList />
      </v-col>
    </v-row>
  </v-container>
</template>
