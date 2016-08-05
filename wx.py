#!/usr/bin/python
import sys
import Adafruit_DHT
import time
import RPi.GPIO as GPIO

button_gpio = 23
sensor_gpio = 4

## Uncomment one of these for your sensor:
# sensor = Adafruit_DHT.DHT11  # Blue
sensor_type = Adafruit_DHT.DHT22  # white
# sensor = Adafruit_DHT.AM2302 # white with wire leads, internal pull-up resistor


GPIO.setmode(GPIO.BCM)

GPIO.setup(button_gpio , GPIO.IN, pull_up_down=GPIO.PUD_UP)


while True:
    print("read temp + humidity")
    humidity, temperature = Adafruit_DHT.read_retry(sensor_type, sensor_gpio)


    # if halt_button:
    #     print ("halt")
    #     sys.exit(0)
    # else:
    #     print ("no halt")


    if humidity is not None and temperature is not None:
        temperature = temperature * 9/5.0 + 32
        print('HO! Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
    else:
        print('no reading')
