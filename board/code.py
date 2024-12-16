import mqtt
import time
import sensor
import encryption
import wifi
import os

# Circuitpython executes this file automatically at startup

def main():
    wifi.radio.connect(os.getenv("CIRCUITPY_WIFI_SSID"), os.getenv("CIRCUITPY_WIFI_PASSWORD"))
    sensor.init_sensor()
    mqtt.connect_broker("192.168.213.58")
            
    while True:
        mqtt.send_message("temperature", encryption.encrypt_message(str(sensor.read_temp())))
        time.sleep(0.1)
        mqtt.send_message("pressure", encryption.encrypt_message(str(sensor.read_pressure())))
        time.sleep(0.1)
        mqtt.send_message("altitude", encryption.encrypt_message(str(sensor.read_altitude())))
        time.sleep(0.1)

if __name__ == "__main__":
    main()