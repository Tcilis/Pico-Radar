import os
import utime
import time
from machine import PWM,Pin
import _thread
servo = PWM(Pin(2))
servo.freq(8)
    
#Set up trigger and echo pins
trig = Pin(22, Pin.OUT)
echo = Pin(21, Pin.IN, Pin.PULL_DOWN)

uart = machine.UART(0, baudrate=9600)
print("UART Info : ", uart)
utime.sleep(3)

servoStop= 1500000
servoForward = 3000000
servoReverse = 600000
# Continuously run the code

def core0_thread():
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
     print ("{:.0f}".format(distance),'cm')
     uart.write(str(distance))
     # Wait for 1 second before taking the next measurement
     time.sleep(1)
     
def core1_thread():
    
    servoStop= 150000
    servoForward = 3500000
    servoReverse = 100000

    while True:
        servo.duty_ns(servoForward)
        utime.sleep(3)
        servo.duty_ns(servoStop)
        utime.sleep(0.2)
        servo.duty_ns(servoReverse)
        utime.sleep(3)
        servo.duty_ns(servoStop)

second_thread = _thread.start_new_thread(core1_thread, ())
core0_thread()