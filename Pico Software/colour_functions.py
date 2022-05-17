import time
import neopixel 

ORDER = neopixel.GRBW

# The number of NeoPixels
num_pixels = 30

def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos * 3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos * 3)
        g = 0
        b = int(pos * 3)
    else:
        pos -= 170
        r = 0
        g = int(pos * 3)
        b = int(255 - pos * 3)
    return (r, g, b) if ORDER in (neopixel.RGB, neopixel.GRB) else (r, g, b, 100)


def rainbow_cycle(pixels, wait):
    for j in range(255):
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(pixel_index & 255)
        pixels.show()
        time.sleep(wait)
        
# https://stackoverflow.com/questions/40312216/converting-rgb-to-rgbw
def rgb_to_rgbw(rgb):
    tM = max(rgb[0], max(rgb[1], rgb[2]))
    
    print(tM)
    
    if tM == 0:
        return (0,0,0,0)
    
    multiplier = 255 / tM
    hR = rgb[0] * multiplier
    hG = rgb[1] * multiplier
    hB = rgb[2] * multiplier
    
    M = max(hR, max(hG, hB))
    m = min(hR, min(hG, hB))
    Luminance = ((M + m) / 2 - 127.5) * (255/127.5) / multiplier
    
    Wo = Luminance
    Ro = rgb[0] - Luminance
    Go = rgb[1] - Luminance
    Bo = rgb[2] - Luminance
    
    if Wo < 0:
        Wo = 0
    if Ro < 0:
        Ro = 0
    if Go < 0:
        Go = 0
    if Bo < 0:
        Bo = 0
    if Wo > 255:
        Wo = 255
    if Ro > 255:
        Ro = 255
    if Go > 255:
        Go = 255
    if Bo > 255:
        Bo = 255
    
    return (Ro, Go, Bo, Wo)
