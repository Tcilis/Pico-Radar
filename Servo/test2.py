from machine import Pin, PWM
import time

# Set up the servo on pin 15
servo = PWM(Pin(15), freq=50)

# Define a function to set the servo angle
def set_angle(angle):
    # Convert the angle to a duty cycle value
    duty = int((angle * 2.5) + 40)
    # Set the servo duty cycle
    servo.duty(duty)

# Continuously rotate the servo between 0 and 120 degrees
while True:
    # Move the servo from 0 to 120 degrees
    for angle in range(0, 121):
        set_angle(angle)
        # Add a small delay to slow down the rotation
        time.sleep(0.01)
    # Move the servo back to 0 degrees
    for angle in range(120, -1, -1):
        set_angle(angle)
        # Add a small delay to slow down the rotation
        time.sleep(0.01)
