# init servo

import utime
from machine import PWM,Pin
servo = PWM(Pin(2))
servo.freq(50)

#define stop,forward and reverse timing in ns
servoStop= 1500000
servoForward = 1000000
servoReverse = 2000000

servo.duty_ns(servoForward)
utime.sleep(2)
servo.duty_ns(servoStop)
utime.sleep(1)
servo.duty_ns(servoReverse)
utime.sleep(2)
servo.duty_ns(servoStop)
