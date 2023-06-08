import os
import time
import _thread
import utime
from servo import Servo
from machine import PWM,Pin

#Set up trigger and echo pins
trig = Pin(21, Pin.OUT)
echo = Pin(22, Pin.IN, Pin.PULL_DOWN)

uart = machine.UART(0, baudrate=9600)
print("UART Info : ", uart)
utime.sleep(3)


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
    s1 = Servo(2)       # Servo pin is connected to GP0

    def servo_Map(x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
 
    def servo_Angle(angle):
        if angle < 0:
            angle = 0
        if angle > 180:
            angle = 180
        s1.goto(round(servo_Map(angle,0,180,0,1024))) # Convert range value to angle value
    
    if __name__ == '__main__':
        while True:	
            for i in range(0,180,1):
                servo_Angle(i)
                utime.sleep(0.1)
            
            for i in range(180,0,-1):
                servo_Angle(i)
                utime.sleep(0.1)


second_thread = _thread.start_new_thread(core1_thread, ())
core0_thread()