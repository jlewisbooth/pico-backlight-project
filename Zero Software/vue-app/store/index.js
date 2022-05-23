const NUM_OF_PIXELS = 30

function formatPixelObject(index) {
  return {
    pixelId: index,
    colour: null,
  }
}

export const state = () => ({
  counter: 0,
  pallette: [],
  maxColours: 8,
})

export const mutations = {
  increment(state) {
    state.counter++
  },
  addColourToPallette(state, colour) {
    if (state.pallette.length < state.maxColours) {
      state.pallette.push(colour)
    }
  },
}
