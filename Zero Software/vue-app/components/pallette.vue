<script>
export default {
  data() {
    return {
      showColourPallette: false,
      selectedColour: '#893492',
      showMenu: false,
    }
  },
  computed: {
    pallette() {
      return this.$store.state.pallette
    },
    counter() {
      return this.$store.state.counter
    },
    maxColours() {
      return this.$store.state.maxCo
    },
  },
  methods: {
    increment() {
      this.$store.commit('increment')
    },
    changeColour(c) {
      console.log(c)

      this.selectedColour = c.hex
    },
    addColourToPallette() {
      console.log('ADD COLOUR', this.showMenu)

      if (this.selectedColour) {
        console.log(this.selectedColour)

        this.$store.commit('addColourToPallette', this.selectedColour)
      }
    },
  },
}
</script>

<template>
  <v-card class="pa-0 ma-3" outlined>
    <v-container class="grey ma-0 pa-0">
      <v-row no-gutters class="pa-0">
        <v-col v-for="palletteOption in pallette" :key="palletteOption">
          <div
            class="pa-2"
            :style="{
              height: '100%',
              'background-color': palletteOption,
              'border-top-right-radius': '0px',
              'border-bottom-right-radius': '0px',
              'border-top-left-radius': '6px',
              'border-bottom-left-radius': '6px',
            }"
          >
            {{ palletteOption }}
          </div>
        </v-col>
        <v-col class="pa-0">
          <v-menu v-model="showMenu" :close-on-content-click="false" offset-y>
            <template v-slot:activator="{ on, attrs }">
              <v-card
                class="pa-12 center add-button"
                ripple
                :outlined="false"
                v-bind="attrs"
                v-on="on"
                :elevation="0"
                flat
                :style="{
                  'border-top-left-radius': '0px',
                  'border-bottom-left-radius': '0px',
                }"
              >
                <v-icon>mdi-plus</v-icon>
              </v-card>
            </template>
            <v-card class="pa-1">
              <v-row>
                <v-col class="pa-9"
                  ><v-color-picker
                    class="ma-0"
                    v-model="selectedColour"
                  ></v-color-picker
                ></v-col>
                <v-col class="pa-9">
                  <v-card
                    class="center pa-2"
                    :style="{
                      height: '100%',
                      'background-color': selectedColour,
                    }"
                  >
                    <v-btn
                      raised
                      large
                      :style="{ 'background-color': 'white' }"
                      @click="addColourToPallette"
                      >Select Colour</v-btn
                    >
                  </v-card>
                </v-col>
              </v-row>
            </v-card>
          </v-menu>
        </v-col>
      </v-row>
    </v-container>
  </v-card>
</template>

<style>
.center {
  justify-content: center;
  align-items: center;
  display: flex;
}

.add-button {
  cursor: pointer;
  box-shadow: none;
}
</style>
