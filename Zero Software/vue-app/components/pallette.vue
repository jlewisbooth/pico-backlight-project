<script>
export default {
  data() {
    return {}
  },
  computed: {
    pallette() {
      return this.$store.state.pallette
    },
    counter() {
      return this.$store.state.counter
    },
  },
  methods: {
    increment() {
      this.$store.commit('increment')
    },
  },
}
</script>

<template>
  <v-card class="pa-2 ma-3" outlined>
    Pallette
    <p>{{ counter }}</p>
    <button @click="increment">Count</button>
    <ul>
      <li v-for="p in pallette" :key="p">
        <span>{{ p }}</span>
      </li>
    </ul>
  </v-card>
</template>

<style>
.container {
  margin: 5px;
}
</style>
