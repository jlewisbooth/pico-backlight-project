<script>
export default {
  name: 'DefaultLayout',
  data() {
    return {
      items: [
        {
          icon: 'mdi-apps',
          title: 'Welcome',
          to: '/',
        },
        {
          icon: 'mdi-chart-bubble',
          title: 'Inspire',
          to: '/inspire',
        },
      ],
      title: 'BackLight',
      showDrawer: false,
    }
  },
  methods: {
    update() {
      console.log(this.mountDrawer)
    },
  },
  computed: {
    mountDrawer() {
      console.log(this)
      switch (this.$vuetify.breakpoint.name) {
        case 'xs':
          return true
        case 'sm':
          return true
        default:
          this.showDrawer = false
          return false
      }
    },
  },
}
</script>
<template>
  <v-app>
    <v-app-bar clipped-right app fixed color="primary" dark>
      <v-toolbar-title v-text="title" />
      <v-spacer />
      <v-app-bar-nav-icon
        v-if="mountDrawer"
        @click.stop="showDrawer = !showDrawer"
      />
    </v-app-bar>
    <v-navigation-drawer
      v-model="showDrawer"
      clipped
      right
      app
      disable-resize-watcher
    >
      <v-list>
        <v-list-item
          v-for="(item, i) in items"
          :key="i"
          :to="item.to"
          router
          exact
        >
          <v-list-item-action>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title v-text="item.title" />
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
    <v-main>
      <Nuxt />
    </v-main>
    <v-footer absolute app color="primary" dark>
      <span
        >&copy; {{ new Date().getFullYear() }}, all rights reserved.. lol</span
      >
    </v-footer>
  </v-app>
</template>
