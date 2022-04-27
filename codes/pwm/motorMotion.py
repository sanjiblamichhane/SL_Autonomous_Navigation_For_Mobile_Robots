import RPi.GPIO as gpio
import wavePWM

#Raspberry Pi Configurations
gpio.setmode(gpio.BCM)
gpio.setwarnings(False)

gpioNo= [2,3,4,17,22,27,10,9,11,5,6,13]
gpio.setup(gpioNo,gpio.OUT)

def mov_dir(x:list):
    for i in range(12):
        gpio.output(gpioNo[i], x[i])

#Constants
fwrd = [0,1,1,1,0,1,0,0,0,0,0,0,]
back = [1,0,1,0,1,1,0,0,0,0,0,0]
left = [0,0,0,0,0,0,1,0,1,0,1,1]
right = [0,0,0,0,0,0,0,1,1,1,0,1]
stop = [0,0,0,0,0,0,0,0,0,0,0,0]
clkw = [0,1,1,0,1,1,0,1,1,0,1,1]
cckw = [1,0,1,1,0,1,1,0,1,1,0,1]

def move(command:str):

    if command == 'w':
        mov_dir(fwrd)

    elif command == 's':
        mov_dir(back)

    elif command == 'a':
        mov_dir(left)

    elif command == 'd':
        mov_dir(right)

    elif command == ' ':
        mov_dir(stop)

    elif command == '/':
        mov_dir(clkw)

    elif command == 'c':
        mov_dir(cckw)

gpio.cleanup()