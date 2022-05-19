import { reactive } from 'vue'
// import DefaultOptions from './default-options'

const NUM_OF_PIXELS = 30

function formatPixelObject(index) {
  return {
    pixelId: index,
    colour: null,
  }
}

export const state = () => ({
  counter: 0,
  pallette: [1, 2, 3],
})

export const mutations = {
  increment(state) {
    state.counter++
  },
}
