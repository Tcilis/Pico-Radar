#ChatGPT
from machine import Pin
import utime

# Define the trigger and echo pins
trigger_pin = Pin(3, Pin.OUT)
echo_pin = Pin(2, Pin.IN)

# Function to measure distance using the ultrasonic sensor
def measure_distance():
    # Send a 10 microsecond pulse to the trigger pin
    trigger_pin.low()
    utime.sleep_us(2)
    trigger_pin.high()
    utime.sleep_us(10)
    trigger_pin.low()

    # Measure the duration of the echo pulse
    while echo_pin.value() == 0:
        pulse_start = utime.ticks_us()
    while echo_pin.value() == 1:
        pulse_end = utime.ticks_us()

    # Calculate the distance using the speed of sound and the duration of the echo pulse
    pulse_duration = pulse_end - pulse_start
    speed_of_sound = 34300  # cm/s
    distance = (pulse_duration / 2) * (speed_of_sound / 1000000)

    return distance

# Test the distance measurement function
while True:
    distance = measure_distance()
    print("Distance: %.2f cm" % distance)
    utime.sleep(1)
