import wifi
import os
import socketpool
import adafruit_minimqtt.adafruit_minimqtt as MQTT
import time

# Based loosely on https://learn.adafruit.com/mqtt-in-circuitpython/circuitpython-wifi-usage
# https://highvoltages.co/iot-internet-of-things/mqtt/image-using-mqtt-protocol/

pool = socketpool.SocketPool(wifi.radio)
mqtt_client = None

def connect_broker(ip_address):
    global mqtt_client
    mqtt_client = MQTT.MQTT(
        broker=ip_address,
        port=1883,
        username="picoW",
        password="picoW",
        recv_timeout=10,
        socket_pool=pool
    )
    
    print(f"Attempting to connect to {ip_address}")
    mqtt_client.connect()
    print(f"Connected to MQTT broker at {ip_address}.")

def send_message(topic, message):
    global mqtt_client
    mqtt_client.publish(topic, message)
