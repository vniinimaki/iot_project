import mqtt
import time
import sensor
import wifi

# Circuitpython executes this file automatically at startup

def main():
    sensor.init_sensor()
    # Need to enter manually, phone wifi assigns new IP everytime it's started
    mqtt.connect_broker("192.168.1.91")
    
    while True:
        mqtt.send_message("temperature", sensor.read_temp())
        mqtt.send_message("pressure", sensor.read_pressure())
        mqtt.send_message("altitude", sensor.read_altitude())
        time.sleep(1)

if __name__ == "__main__":
    main()