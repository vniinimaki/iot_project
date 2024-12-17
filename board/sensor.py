import busio
import board
import time
import digitalio
import adafruit_bmp280

i2c = None
bmp280 = None
led = None

def init_sensor():
    global i2c
    global bmp280
    global led
    
    i2c = busio.I2C(board.GP1, board.GP0) # SCL, SDA
    
    bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c, address=0x76)
    bmp280.sea_level_pressure = 1000
    
    led = digitalio.DigitalInOut(board.LED)
    led.direction = digitalio.Direction.OUTPUT
    
    print("Sensor initialized")
    
def read_temp():
    global bmp280
    global led
    
    if (bmp280.temperature > 24):
        led.value = True
    else:
        led.value = False
            
    return bmp280.temperature

def read_altitude():
    global bmp280
    return bmp280.altitude

def read_pressure():
    global bmp280
    return bmp280.pressure