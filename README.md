# IoT based Weather Station

## Overview

This project is a lightweight IoT-based weather monitoring system developed using CircuitPython. It reads temperature, pressure, and altitude data from a sensor, encrypts the data, and transmits it over MQTT to a broker. The project is optimized for devices such as the Raspberry Pi Pico W and is configured to activate an LED indicator if the temperature exceeds a specified threshold.




## Project Functionalities
- Real-Time Weather Monitoring: Measure environmental data using the BMP280 sensor to collect
  - Temperature
  - Pressure
  - Altitude
- Secure Data Transmission: Encrypt sensor data using AES encryption prior to publishing it to an MQTT broker.
- Connectivity: Communicate over a WiFi network and send data to a specified MQTT broker.
- Control Output: Built-in LED lights up if the temperature exceeds a specified threshold.



## Source Code Structure

 - code.py         # Main execution file; connects to WiFi, reads sensor data, encrypts, and publishes to MQTT
 - encryption.py   # AES encryption logic for securing messages
 - mqtt.py         # Handles MQTT broker connection and message publishing
 - sensor.py       # Initializes and reads data from the BMP280 sensor
 - settings.toml   # stores wifi credentials

## Setup and Deployment
- Requirements
  - Hardware:
    - Raspberry Pi Pico W
    - BMP280 Sensor

  - Software:
    - CircuitPython libraries:
     - adafruit_minimqtt
     - adafruit_bmp280
     - aesio

## Debugging and Troubleshooting

- WiFi Issues:

    Ensure correct SSID and password, and check if the network allows device connections.

- MQTT Connection Failures:

    Verify the broker IP address and port and  the broker is running and reachable.


  **note** : Use debug mode (DEBUG = 1) in encryption.py for testing.
