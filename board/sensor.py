import busio
import board
import time
import adafruit_bmp280

i2c = None
bmp280 = None

def init_sensor():
    global i2c
    global bmp280
    i2c = busio.I2C(board.GP1, board.GP0) # SCL, SDA
    
    bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c, address=0x76)
    bmp280.sea_level_pressure = 1013.25
    
    print("Sensor intialized")
    
def read_temp():
    global bmp280
    temp = bmp280.temperature
    return temp

def read_pressure():
    global bmp280
    pressure = bmp280.pressure
    return pressure