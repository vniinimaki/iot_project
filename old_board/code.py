import mqtt
import capture_image as image
import time

# Circuitpython executes this file automatically at startup

def main():
    # Need to enter manually, phone wifi assigns new IP everytime it's started
    mqtt.connect_broker("192.168.187.236")
    
    while True:
        # Send messages as fast as possible, linearly
        image.capture_image()
        
        # ML thing here i guess
        # get the %detection from ML
        # or just send the image to mqtt if ML on laptop
        
        message = "Person detection confidence: 69%"
        # Send the current image
        mqtt.send_image("photobin.txt")
        mqtt.send_message(message)
        time.sleep(1)

if __name__ == "__main__":
    main()