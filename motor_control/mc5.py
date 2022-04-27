import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)
gpio.setwarnings(False)

gpio.setup(5, gpio.OUT)
gpio.setup(18, gpio.OUT)
gpio.setup(28, gpio.OUT)
gpio.setup(23, gpio.OUT)
gpio.setup(3, gpio.OUT)
gpio.setup(4, gpio.OUT)
gpio.setup(11, gpio.OUT)
gpio.setup(10, gpio.OUT)
gpio.setup(12, gpio.OUT)
gpio.setup(6, gpio.OUT)
gpio.setup(7, gpio.OUT)
gpio.setup(14, gpio.OUT)


gpio.output(5, True)
gpio.output(18, False)
gpio.output(23, False)
gpio.output(28, True)
gpio.output(3, True)
gpio.output(4, False)
gpio.output(11, True)
gpio.output(10, False)
gpio.output(12, True)
gpio.output(6, True)
gpio.output(7, True)
gpio.output(14, False)

i = '1'

while (True):
    i = input()

    if i == 'w':
        gpio.output(3, False)
        gpio.output(4, True)
        gpio.output(5, True)
        gpio.output(18, True)
        gpio.output(28, False)
        gpio.output(23, True)
        
        gpio.output(11, False)
        gpio.output(10, False)
        gpio.output(12, False)
        gpio.output(6, False)
        gpio.output(7, False)
        gpio.output(14, False)

    elif i == 's':
        gpio.output(3, True)
        gpio.output(4, False)
        gpio.output(5, True)
        gpio.output(18, False)
        gpio.output(28, True)
        gpio.output(23, True)
        
        gpio.output(11, False)
        gpio.output(10, False)
        gpio.output(12, False)
        gpio.output(6, False)
        gpio.output(7, False)
        gpio.output(14, False)

    elif i == 'a':
        gpio.output(3, False)
        gpio.output(4, False)
        gpio.output(5, False)
        gpio.output(18, False)
        gpio.output(28, False)
        gpio.output(23, False)
        
        gpio.output(11, True)
        gpio.output(10, False)
        gpio.output(12, True)
        gpio.output(6, False)
        gpio.output(7, True)
        gpio.output(14, True)

    elif i == 'd':
        gpio.output(3, False)
        gpio.output(4, False)
        gpio.output(5, False)
        gpio.output(18, False)
        gpio.output(28, False)
        gpio.output(23, False)
        
        gpio.output(11, False)
        gpio.output(10, True)
        gpio.output(12, True)
        gpio.output(6, True)
        gpio.output(7, False)
        gpio.output(14, True)

    elif i == '1':
        gpio.output(3, False)
        gpio.output(4, False)
        gpio.output(5, False)
        gpio.output(18, False)
        gpio.output(28, False)
        gpio.output(23, False)
        
        gpio.output(11, False)
        gpio.output(10, False)
        gpio.output(12, False)
        gpio.output(6, False)
        gpio.output(7, False)
        gpio.output(14, False)
    
    else:
        break

##
time.sleep(1.5)

gpio.cleanup()


        
