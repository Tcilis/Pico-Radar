#https://www.tomshardware.com/how-to/raspberry-pi-pico-ultrasonic-sensor
from machine import Pin
import utime

# Define the trigger and echo pins
trigger = Pin(3, Pin.OUT)
echo = Pin(2, Pin.IN)

# Define the function to measure distance
def ultra():
   trigger.low()  # Set trigger pin to low
   utime.sleep_us(2)  # Wait for 2 microseconds
   trigger.high()  # Set trigger pin to high
   utime.sleep_us(5)  # Wait for 5 microseconds
   trigger.low()  # Set trigger pin to low again
   while echo.value() == 0:  # Wait for echo pin to go high
       signaloff = utime.ticks_us()
   while echo.value() == 1:  # Wait for echo pin to go low again
       signalon = utime.ticks_us()
   timepassed = signalon - signaloff  # Calculate time passed
   distance = (timepassed * 0.0343) / 2  # Calculate distance in cm
   print("The distance from object is ",distance,"cm")

# Run the function in a loop
while True:
   ultra()
   utime.sleep(1)  # Wait for 1 second before running the function again
