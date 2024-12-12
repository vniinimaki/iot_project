import wifi
import os
import socketpool
import adafruit_minimqtt.adafruit_minimqtt as MQTT
import time

# Based on https://learn.adafruit.com/mqtt-in-circuitpython/circuitpython-wifi-usage

chunkSize = 1024
pool = socketpool.SocketPool(wifi.radio)

def sendImage(pathToImage):
    # Image has to be sent in chunks, probably library limitation, only 2kb file worked during testing
    # Calculate the number of chunks needed for a given file
    imageSize = os.stat(pathToImage)[6]
    mqtt_client.publish("imageSize", imageSize)
    mqtt_client.publish("text", "amogus")
    
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


mqtt_client = MQTT.MQTT(
    broker="192.168.187.236",
    port=1883,
    socket_pool=pool
)

mqtt_client.connect()

print("Connected to MQTT broker.")

sendImage("GeZTI9XW0AAL3OY.jpg")


