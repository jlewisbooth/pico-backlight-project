import board
import digitalio
import time
import neopixel
import busio
import adafruit_rfm69
from colour_functions import rainbow_cycle, rgb_to_rgbw

# ============= Radio Set-Up =================

RADIO_FREQ_MHZ   = 915.0

# Define pins connected to the chip.
cs = digitalio.DigitalInOut(board.GP6)
reset = digitalio.DigitalInOut(board.GP7)

spi = busio.SPI(board.GP2, MOSI=board.GP3, MISO=board.GP4)

# Initialze RFM radio
rfm69 = adafruit_rfm69.RFM69(spi, cs, reset, RADIO_FREQ_MHZ)

# Optionally set an encryption key (16 byte AES key). MUST match both
# on the transmitter and receiver (or be set to None to disable/the default).
rfm69.encryption_key = b'\x01\x02\x03\x04\x05\x06\x07\x08\x01\x02\x03\x04\x05\x06\x07\x08'

rfm69.enable_crc = True
# set delay before transmitting ACK (seconds)
rfm69.ack_delay = 0.1

rfm69.node = 2
rfm69.destination = 1

#initialize flag and timer
last_xmit = 0
xmit_interval = 10

# =========================================================================================

# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.GP0

# The number of NeoPixels
num_pixels = 30

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRBW

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=1.0, auto_write=False, pixel_order=ORDER
)

colour = rgb_to_rgbw([255, 255, 20])

print(colour)

def updateError(dt):
    for j in range(256):
        pixels.fill(255 - j, 0, 0, 0)
        pixels.show()
        time.sleep(dt)
    

def updatePixels(bArr):
    msg = bArr.decode("utf-8")

while True:
    
    packet = rfm69.receive(with_ack=True, with_header=True)

    print("TIMEOUT")
    
    if packet is not None:
        # Received a packet!
        # Print out the raw bytes of the packet:
        print('Received (raw header):', [hex(x) for x in packet[0:4]])
        print('Received (raw payload): {0}'.format(packet[4:]))
        # send reading after any packet received
        # pixels.fill((0, 255, 0, 0))
        # pixels.show()
        
        # updateError(0.02)
        
    # if time.monotonic() - last_xmit > xmit_interval:
        # rfm69.send(bytes("Hello World","utf-8"))
        # last_xmit = time.monotonic()
        # pixels.fill((0, 0, 255, 0))
        # pixels.show()

    # rainbow_cycle(pixels, 0.001)  # rainbow cycle with 1ms delay per step

    
    
