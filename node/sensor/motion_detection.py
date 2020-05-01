#!/usr/bin/env python3

import signal
import sys
import RPi.GPIO as GPIO
import requests
import json
from threading import Timer


#if pins are rearranged on the pi, change the values corresponding to the
#correct pins
SENSOR_PIN = 36
SENSOR2_PIN = 31
SENSOR3_PIN = 33
SENSOR4_PIN = 37
LED_PIN = 32

global BRAIN_MOTION_URL
# global LIGHT
global timer

def signal_handler(sig, frame):
    GPIO.cleanup()
    sys.exit(0)


def sensor_callback(channel):
    global timer

    if((GPIO.input(SENSOR_PIN)==1) or (GPIO.input(SENSOR2_PIN)==1) or (GPIO.input(SENSOR3_PIN)==1) or (GPIO.input(SENSOR4_PIN)==1)):
        turn_on_light()
        try:
            requests.post(str(BRAIN_MOTION_URL),json=json.dumps({"value":"1"}))
        except:
            pass
    if((GPIO.input(SENSOR_PIN) == 0) and (GPIO.input(SENSOR2_PIN) == 0) and  (GPIO.input(SENSOR3_PIN) == 0) and  (GPIO.input(SENSOR4_PIN) == 0)):
        with open("config.json","r+") as f:
            x = json.load(f)
            LIGHT = int(x["light_time"])
        if(LIGHT>0):
            print("startin timer")
            print(LIGHT)
            timer = Timer(LIGHT, turn_off_light)
            timer.start()
        try:
            requests.post(str(BRAIN_MOTION_URL),json=json.dumps({"value":"0"}))
        except:
            pass


def turn_on_light():
    GPIO.output(LED_PIN, GPIO.HIGH)
    

def turn_off_light():
    print("turning off light")
    GPIO.output(LED_PIN,GPIO.LOW)


def main():
    with open("config.json","r+") as f:
        x = json.load(f)
    global BRAIN_MOTION_URL
    # global LIGHT
    # LIGHT = int(x["light_time"])
    BRAIN_MOTION_URL= "http://"+x["brain_ip"]+":"+x["brain_port"]+"/api/motion_sensor"
    #set board pin numbering to the numbers of the pins
    # print("turning on motion sensors")
    print(BRAIN_MOTION_URL)
    GPIO.setmode(GPIO.BOARD)

    #setup led pin
    GPIO.setup(LED_PIN, GPIO.OUT)  
    GPIO.output(LED_PIN,GPIO.LOW)

    #setup sensor 1 input and interrupt handler
    GPIO.setup(SENSOR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(SENSOR_PIN, GPIO.BOTH,callback=sensor_callback)

    #setup sensor 2 input and interrupt handler
    GPIO.setup(SENSOR2_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(SENSOR2_PIN, GPIO.BOTH,callback=sensor_callback)

    #setup sensor 3 input and interrupt handler
    GPIO.setup(SENSOR3_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(SENSOR3_PIN, GPIO.BOTH,callback=sensor_callback)

    #setup sensor 4 input and interrupt handler
    GPIO.setup(SENSOR4_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(SENSOR4_PIN, GPIO.BOTH,callback=sensor_callback)

    signal.signal(signal.SIGINT, signal_handler)    
    signal.pause()

if __name__ == "__main__":
    main()