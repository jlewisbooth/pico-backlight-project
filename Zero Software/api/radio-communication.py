import board
import busio
import digitalio
import adafruit_rfm69

RADIO_FREQ_MHZ   = 915.0

# Define pins connected to the chip.
cs = digitalio.DigitalInOut(board.D24)
reset = digitalio.DigitalInOut(board.D23)

spi = busio.SPI(board.D11, MOSI=board.D10, MISO=board.D9)

# Initialze RFM radio
rfm69 = adafruit_rfm69.RFM69(spi, cs, reset, RADIO_FREQ_MHZ)

# Optionally set an encryption key (16 byte AES key). MUST match both
# on the transmitter and receiver (or be set to None to disable/the default).
rfm69.encryption_key = b'\x01\x02\x03\x04\x05\x06\x07\x08\x01\x02\x03\x04\x05\x06\x07\x08'

rfm69.ack_delay = None

rfm69.node = 1
rfm69.destination = 2

# Wait to receive packets.
print('Waiting for packets...')

#initialize flag and timer
last_xmit = 0
xmit_interval = 10

# initialize counter
counter = 0
ack_failed_counter = 0

def formatColour(str):
    try:
        rgb = str.split(",")

        if len(rgb) != 3:
            raise Exception("Need three numbers for rgb.")

        r = int(rgb[0])
        g = int(rgb[1])
        b = int(rgb[2])

        if not type(r) is int:
            raise TypeError("Only Integers Allowed.")

        if not type(g) is int:
            raise TypeError("Only Integers Allowed.")
        
        if not type(b) is int:
            raise TypeError("Only Integers Allowed.")

        if r > 255 or r < 0:
            raise ValueError("Each number needs to be between 0 and 255.")

        if g > 255 or g < 0:
            raise ValueError("Each number needs to be between 0 and 255.")

        if b > 255 or b < 0:
            raise ValueError("Each number needs to be between 0 and 255.")

        return (r,g,b)
    except TypeError as err:
        print("Type Error: {0}".format(err))
        return None
    except ValueError as err:
        print("Value Error: {0}".format(err))
        return None
    except Exception as err:
        print("Exception: {0}".format(err))
        return None

def joinRGB(arr):
    formattedStr = ""
    for index, item in enumerate(arr):
        formattedStr += str(item)

        if index != len(arr) - 1:
            formattedStr += ","
        else:
            formattedStr += "|"
    
    return formattedStr

while True:
    # Look for a new packet: only accept if addresses to my_node
    print('Listening...')

    val = input("What colour to fill neoPixels with (format: r,g,b): ")
    colour = formatColour(val)
    
    # packet = rfm69.receive(with_header=True, timeout=5.0)
    
    msg = joinRGB(colour)

    if not rfm69.send_with_ack(
            bytes("{}".format(msg), "UTF-8")
        ):
            ack_failed_counter += 1
            print(" No Ack: ", counter, ack_failed_counter)

    # if packet is not None:
    #     print('Received (raw header):', [hex(x) for x in packet[0:4]])
    #     print('Received (raw payload): {0}'.format(packet[4:]))
    # if time.monotonic() - last_xmit > xmit_interval:
    #     rfm69.send(bytes("Hello World","utf-8"))
    #     last_xmit = time.monotonic()