# Help with understanding PICO code uploads

Boot the pico with the BOOTSEL button pressed, copy the main.py to the Pico, then disconnect/reconnect to run the main.py. This clearly doesn't work though, because it is wrong. BOOTSEL mode is ONLY to update the UF2 file (or Circuit Python UF2 file in this case).

If you boot the Pico in BOOTSEL mode, you get to see a volume mounted, and it's obvious (BUT WRONG) to think that this is where you dump your main.py file.

If you connect your Pico without BOOTSEL pressed, you don't get to see the Pico as a mounted device, and Thonny doesn't initially appear to give the option to save (or run) a program on the Pico. The answer is behind that unassuming button (that doesn't look at all like a button) in the bottom right-hand corner of Thonny, which allows one to Configure Interpreter. It will just read "Python 3.7" or something like that. That button is the key.

The following procedure assumes that you have already booted your Pico in BOOTSEL mode, copied on a UF2 file, and then disconnected your Pico. BTW, I must have copied twenty or more UF2 files onto my Pico before I figured out the next bit, so don't worry if you've done that a few times already - it's not a bad thing, you won't have hurt the Pico, and you probably should do this from time to time anyway to keep the firmware up to date. ;)

The Procedure

- Connect your Pico using a USB Data cable\*, NOT in BOOTSEL mode - Don't touch that button! Don't even look at it aggressively.
- Start Thonny
- Left-click the Python button in the bottom right-hand corner, and choose 'Configure interpreter'
- Select interpreter - "CircuitPython (Raspberry Pi Pico)"
- Select Port - "Board in FS mode - Board CDC (/dev/ttyACM0)
- Click OK

You should now be able to write scripts, and save them to the Pico. If you have an existing code window open and find that the Save button does not give that option, try copying all of the code to a fresh window and trying to save it from there. Don't forget, your Pico program must be called main.py even if it imports code from other .py scripts.

I strongly suggest you run the code after saving to be sure it executes. If there is a bug, either in the logic or syntax, it is easy to spot now. It may not be later.

After that you should be able to disconnect your Pico and then plug it in to a power source (either the same computer you just programmed it from, or for example a USB power bank, or USB mains adapter), and the code will just run.

When you reconnect the Pico to your (programming) computer, the Pico code will start executing, and when you open Thonny and then open the main.py on the Pico you can click the Stop button to end execution of main.py on the Pico
