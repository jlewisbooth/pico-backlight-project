import board
import busio
import digitalio
import adafruit_rfm69
import time

RADIO_FREQ_MHZ   = 915.0

# Define pins connected to the chip.
cs = digitalio.DigitalInOut(board.D5)
reset = digitalio.DigitalInOut(board.D6)

spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)

# Initialze RFM radio
rfm69 = adafruit_rfm69.RFM69(spi, cs, reset, RADIO_FREQ_MHZ)

# Optionally set an encryption key (16 byte AES key). MUST match both
# on the transmitter and receiver (or be set to None to disable/the default).
rfm69.encryption_key = b'\x01\x02\x03\x04\x05\x06\x07\x08\x01\x02\x03\x04\x05\x06\x07\x08'

rfm69.ack_delay = None
# Wait to receive packets.
print('Waiting for packets...')
#initialize flag and timer
last_xmit = 0
xmit_interval = 10

while True:
    # Look for a new packet: only accept if addresses to my_node
    print('Listening...')
    packet = rfm69.receive(with_header=True)
    # If no packet was received during the timeout then None is returned.
    print('Timeout!')
    
    if packet is not None:
        # Received a packet!
        # Print out the raw bytes of the packet:
        print('Received (raw header):', [hex(x) for x in packet[0:4]])
        print('Received (raw payload): {0}'.format(packet[4:]))
        # send reading after any packet received
    if time.monotonic() - last_xmit > xmit_interval:
        rfm69.send(bytes("Hello World","utf-8"))
        last_xmit = time.monotonic()
