import mqtt
import time

# Circuitpython executes this file automatically at startup

def main():
    # Need to enter manually, phone wifi assigns new IP everytime it's started
    mqtt.connect_broker("192.168.187.58")
    
    while True:
        
        mqtt.send_message("temperature", "33852")
        mqtt.send_message("pressure", "3")
        return

if __name__ == "__main__":
    main()