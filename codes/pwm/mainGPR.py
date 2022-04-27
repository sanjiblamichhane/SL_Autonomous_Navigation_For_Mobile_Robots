import motorMotion
import readPWM
import time

#Constants
validEncVal= [14,15,23,24,8,7,20,21]

print("Starting MainGPR:")
while(True):

    command = input("Please Enter Command:")

    if command == 'wpwm':
        print("Enter new Duty Cycle and Frequency:")
        dutyCycle= float(input())
        freq= float(input())
        print("Duty cycle and Frequency Updated")

    elif command == 'rpwm':
        print("Enter Encoder value:")
        pinNo= int(input())

        if pinNo in validEncVal:
            readPWM.printPWM(pinNo)

        else:
            print("Not a valid Encoder value:")

    elif command == 'exit':
        motorMotion.move(' ')
        print("Program about to Stop")
        break

    else:
        motorMotion.move(command)

    time.sleep(0.5)

print("Finishing Main GPR")
time.sleep(1)