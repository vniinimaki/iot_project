import wifi
import os
import socketpool
import adafruit_minimqtt.adafruit_minimqtt as MQTT
import time

# Based loosely on https://learn.adafruit.com/mqtt-in-circuitpython/circuitpython-wifi-usage
# https://highvoltages.co/iot-internet-of-things/mqtt/image-using-mqtt-protocol/

chunkSize = 1024
pool = socketpool.SocketPool(wifi.radio)
mqtt_client = None

def connect_broker(ip_address):
    global mqtt_client
    mqtt_client = MQTT.MQTT(
        broker=ip_address,
        port=1883,
        username="picoW",
        password="picoW",
        socket_pool=pool
    )
    
    print(f"Attempting to connect to {ip_address}")
    mqtt_client.connect()
    print(f"Connected to MQTT broker at {ip_address}.")

def send_image(pathToImage):
    global mqtt_client
    # Image has to be sent in chunks, probably library limitation, only 2kb file worked during testing
    # Calculate the number of chunks needed for a given file
    imageSize = os.stat(pathToImage)[6]
    mqtt_client.publish("imageSize", imageSize)
    
    numberOfChunks = int(imageSize/chunkSize + 1)
    
    # Send number of chunks to tell JavaScript how many chunks are coming
    mqtt_client.publish("chunkSize", numberOfChunks)
    
    with open(pathToImage, "rb") as file:
        chunk = file.read(chunkSize)
        while chunk:
            b = bytes(chunk)
            mqtt_client.publish("images", b)
            chunk = file.read(chunkSize)
    
    print(f"Image sent as {numberOfChunks} chunks")

def send_message(message):
    global mqtt_client
    mqtt_client.publish("text", message)
    print(f"Sent: {message}")
