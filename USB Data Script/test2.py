import os
import utime
from machine import Pin
import time

# Set up trigger and echo pins
trig = Pin(17, Pin.OUT)
echo = Pin(16, Pin.IN, Pin.PULL_DOWN)

uart = machine.UART(0, baudrate=9600)
print("UART Info : ", uart)
utime.sleep(3)

# Continuously run the code
while True:
     # Set trigger pin to low to ensure a clean start
     trig.value(0)
     # Wait for 100 milliseconds before sending the trigger signal to the sensor to avoid interference
     time.sleep(0.1)
     # Send a 10 microsecond pulse to the trigger pin
     trig.value(1)
     time.sleep_us(2)
     trig.value(0)
     # Measure the duration of the echo pulse
     while echo.value()==0:
          pulse_start = time.ticks_us()
     while echo.value()==1:
          pulse_end = time.ticks_us()
     pulse_duration = pulse_end - pulse_start
     # Calculate distance from pulse duration
     distance = pulse_duration * 17165 / 1000000
     distance = round(distance, 0)
     # Print the distance in centimeters
     print ('Distance:',"{:.0f}".format(distance),'cm')
     uart.write(str(distance))
     # Wait for 1 second before taking the next measurement
     time.sleep(1)