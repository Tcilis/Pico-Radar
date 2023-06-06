# http://stackoverflow.com/questions/44056846/ddg#44056921

# For windows "pip install pyserial"

import serial
import time

serialPort = serial.Serial(
    port="COM3", baudrate=9600, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE
)
serialString = ""  # Used to hold data coming over UART
while 1:
    # Wait until there is data waiting in the serial buffer
    if serialPort.in_waiting > 0:

        # Read data out of the buffer until a carraige return / new line is found
        serialString = serialPort.readline()

        # Print the contents of the serial data
        try:
            print(serialString.decode("Ascii"))
            with open("C:\\Users\\User\\Desktop\\data.txt", 'w') as f:
                f.write(serialString.decode("Ascii"))

        except:
            pass