import board
import busio
from adafruit_ov7670 import OV7670, OV7670_SIZE_DIV4, OV7670_TEST_PATTERN_COLOR_BAR
from ulab import numpy
from displayio import Bitmap
import time

def capture_image():


    debug = 1
    """
    Captures an image using the OV7670 camera and prints the image data to serial output and writes it to a binary file
    """
    # Initialize I2C bus
    i2c = busio.I2C(scl=board.GP9, sda=board.GP8)

    # Initialize the OV7670 camera
    cam = OV7670(
        i2c,
        data_pins=[
            board.GP12, board.GP13, board.GP14, board.GP15,
            board.GP16, board.GP17, board.GP18, board.GP19
        ],
        clock=board.GP11,
        vsync=board.GP7,
        href=board.GP21,
        mclk=board.GP20,
        shutdown=None,
        reset=board.GP10,
    )

    # Set camera resolution
    cam.size = OV7670_SIZE_DIV4

    # Create a buffer to store the captured image
    buf = bytearray(4 * cam.width * cam.height)
    # Capture an image
    cam.capture(buf)
    try:
        with open("photobin.txt", "wb") as photo:
            temp = buf
            photo.write(temp)
            print(temp)
            photo.flush()
            time.sleep(1)
            
    except OSError as e:
        print("error")
