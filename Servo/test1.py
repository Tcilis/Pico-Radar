#ChatGPT
import machine
import utime

# initialize PWM object
pwm = machine.PWM(machine.Pin(2))

# set frequency to 50 Hz (typical for servo motors)
pwm.freq(50)

# define pulse width range (typically 500-2500 microseconds)
min_us = 500
max_us = 2500

# define function to set servo position
def set_servo_position(angle):
    # convert angle to pulse width between min_us and max_us
    us = min_us + int((max_us - min_us) * angle / 120)
    # set duty cycle based on pulse width
    pwm.duty_us(us)

# rotate servo to starting position (60 degrees)
set_servo_position(60)

# rotate servo back and forth between 0 and 120 degrees
while True:
    for angle in range(0, 121, 1):
        set_servo_position(angle)
        utime.sleep_ms(10)
    for angle in range(120, -1, -1):
        set_servo_position(angle)
        utime.sleep_ms(10)
