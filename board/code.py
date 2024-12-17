import mqtt
import time
import sensor
import encryption
import wifi
import os

# Circuitpython executes this file automatically at startup

def send_test():
    mqtt.send_message("temperature", encryption.pad_to(str(sensor.read_temp()), 1024))
    time.sleep(0.1)
    mqtt.send_message("pressure", encryption.pad_to(str(sensor.read_pressure()), 1024))
    time.sleep(0.1)
    mqtt.send_message("altitude", encryption.pad_to(str(sensor.read_altitude()), 1024))
    time.sleep(0.1)
    
def send_sensors_encrypted():
    mqtt.send_message("temperature", encryption.encrypt_message(str(sensor.read_temp())))
    time.sleep(0.1)
    mqtt.send_message("pressure", encryption.encrypt_message(str(sensor.read_pressure())))
    time.sleep(0.1)
    mqtt.send_message("altitude", encryption.encrypt_message(str(sensor.read_altitude())))
    time.sleep(0.1)
    
def send_sensors():
    mqtt.send_message("temperature", str(sensor.read_temp()))
    time.sleep(0.1)
    mqtt.send_message("pressure", str(sensor.read_pressure()))
    time.sleep(0.1)
    mqtt.send_message("altitude", str(sensor.read_altitude()))
    time.sleep(0.1)

def main():
    wifi.radio.connect(os.getenv("CIRCUITPY_WIFI_SSID"), os.getenv("CIRCUITPY_WIFI_PASSWORD"))
    sensor.init_sensor()
    mqtt.connect_broker("192.168.213.58")
            
    while True:
        # Unencrypted messages require changes in the JS to display the values
        # send_test()
        # send_sensors()
        send_sensors_encrypted()

if __name__ == "__main__":
    main()