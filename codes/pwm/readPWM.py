import time
import RPi.GPIO as gpio
print("Starting PWM Readings")

def printPWM(PinNo:int):

    gpio.setup(PinNo,gpio.IN)

    #Some in-function Constants
    t0_ref=0
    t0=0
    t1_ref=0
    t1=0
    val0= 1
    val1= 1
    count=0
    span=5
    cond =1

    while(cond):

        val1 = gpio.input(PinNo)

        if (val0 == 0) and (val1 == 1):
            cond=0
            t1_ref = time.time()
            print('Starting Count:')

        val0 = val1
        time.sleep(0.001)

    while (count<span):

        val1= gpio.input(PinNo)

        if (val0==0) and (val1==1):
            count += 1
            t0 += time.time() - t0_ref
            t1_ref = time.time()

        elif (val0==1) and (val1==0):
            t1 += time.time() - t1_ref
            t0_ref = time.time()

        else:
            pass

        val0=val1
        time.sleep(0.001)

    t0 /= span
    t1 /= span

    print("The PWM wave has the following properties:")
    print("Period: ", end='')
    print(t1+t0)
    print("Duty Cycle: ",end='')
    print(t1/(t1+t0))
    print("Frequency: ",end='')
    print(1/(t1+t0))