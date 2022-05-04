import motorMotion
import readPWM
import time
import RPi.GPIO as gpio
import wavePWM 
import pigpio

## o
pi = pigpio.pi()
#Raspberry Pi Configurations
gpio.setmode(gpio.BCM)
gpio.setwarnings(False)

gpioNo= [2,3,4,17,22,27,10,9,11,5,6,13]
EncVals= [14,23,8,20]
motorVals= ['a','b','c','d']
pwmVals= [7,15,23,33]

gpio.setup(gpioNo,gpio.OUT)


print("Starting MainGPR:")
while(True):

    command = input("Please Enter Command:")

    if command == 'wpw':
        print("Enter Motor for PWM:")
        pinNo= input()

        if pinNo in motorVals:
            pinNo = pwmVals[motorVals.index(pinNo)]

            print("Enter new Duty Cycle and Frequency:")
            dutyCycle= float(input())
            freq= float(input())
            pwm= wavePWM.PWM(pi)
            pwm.set_frequency(freq)
            pwm.set_pulse_start_in_fraction(pinNo,0)
            pwm.set_pulse_length_in_fraction(pinNo,dutyCycle)
            pwm.update()
            print("Duty cycle and Frequency Updated")
        else:
            print("Invalid Input")

    elif command == 'rpw':
        print("Enter Encoder value:")
        pinNo= input()

        if pinNo in motorVals:
            pinNo = EncVals[motorVals.index(pinNo)]
            readPWM.printPWM(pinNo)

        else:
            print("Not a valid input")

    elif command == 'exit':
        motorMotion.move(' ')
        print("Program about to Stop")
        break

    else:
        motorMotion.move(command)

    time.sleep(0.5)

print("Finishing Main GPR")
time.sleep(1)