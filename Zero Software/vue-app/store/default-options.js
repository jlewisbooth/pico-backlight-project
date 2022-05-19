const NUM_OF_PIXELS = 30

const DEFAULT_OPTIONS = [
  {
    optionId: 'default-option-1',
    displayName: 'Test Option',
    pallette: [
      {
        colourIndex: 1,
        colour: '#ff0000',
      },
      {
        colourIndex: 2,
        colour: '#ffffff',
      },
    ],
    pixels: Array(NUM_OF_PIXELS).map((_, i) => {
      if (i % 2) {
        return {
          pixelId: i,
          colour: '#ff0000',
        }
      } else {
        return {
          pixelId: i,
          colour: '#ffffff',
        }
      }
    }),
  },
]

export default DEFAULT_OPTIONS
