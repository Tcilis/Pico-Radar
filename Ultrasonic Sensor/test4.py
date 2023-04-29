from machine import Pin
import utime

# Set up trigger and echo pins for HC-SR04+ sensor
trigger = Pin(3, Pin.OUT)
echo = Pin(2, Pin.IN)

def get_distance():
    # Send a 10us pulse to trigger the sensor
    trigger.low()
    utime.sleep_us(2)
    trigger.high()
    utime.sleep_us(10)
    trigger.low()
    
    # Wait for the echo pin to go high and record the time
    while echo.value() == 0:
        signaloff = utime.ticks_us()
    # Wait for the echo pin to go low and record the time
    while echo.value() == 1:
        signalon = utime.ticks_us()
    
    # Calculate the time difference between the two recorded times
    timepassed = signalon - signaloff
    # Calculate the distance using the speed of sound (343m/s)
    distance = (timepassed * 0.0343) / 2
    
    # Return the calculated distance
    return distance

# Main loop of the program
while True:
    # Call the get_distance() function and print the result
    print(get_distance())
    # Wait for 1 second before repeating
    utime.sleep(1)
