#!/usr/bin/env python
import psutil
import RPi.GPIO as GPIO
from time import sleep

def myCycle(pwm):
    pwm.start(0)
    for x in range(100):    # This Loop will run 100 times
        pwm.ChangeDutyCycle(x) # Change duty cycle
        sleep(0.01)         # Delay of 10mS      
    for x in range(100,0,-1): # Loop will run 100 times; 100 to 0
        pwm.ChangeDutyCycle(x)
        sleep(0.01)
    pwm.stop()
  

#init
led_pin = 12
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led_pin, GPIO.OUT)

pwm = GPIO.PWM(led_pin, 1000)

#main
while 1:
    cpu = psutil.cpu_percent()
    print(cpu)
    if (cpu > 35.0): 
        myCycle(pwm)
    else:
        GPIO.output(led_pin, GPIO.LOW)
        sleep(2)
