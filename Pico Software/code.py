import time
import board
import neopixel
from _pixelbuf import colorwheel

# Update this to match the number of NeoPixel LEDs connected to your board.
num_pixels = 30

pixels = neopixel.NeoPixel(board.GP0, num_pixels, pixel_order=neopixel.RGBW)
pixels.brightness = 1

def rainbow(speed):
    for j in range(255):
        print(j)
        for i in range(num_pixels):
            pixel_index = j
            pixels[i] = colorwheel(pixel_index & 255)
        pixels.show()
        time.sleep(speed)


while True:
    rainbow(.05)