import RPi.GPIO as GPIO

import time

def dec2bin(value):
 
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

def num2dac(value):
    signal = dec2bin(value)
    GPIO.output(dac,signal)

def binary_search_recursive(array, element, start, end):
    if start > end:
        return -1

    mid = (start + end) // 2
    if element == array[mid]:
        return mid

    if element < array[mid]:
        return binary_search_recursive(array, element, start, mid-1)
    else:
        if start > end:
            return -1

GPIO.setmode(GPIO.BCM)

clean =[0,0,0,0,0,0,0,0]
dac = [26,19,13,6,5,11,9,10]
comp = 4
troyka = 17
GPIO.setup(troyka,GPIO.OUT,initial = 1)
GPIO.setup(dac,GPIO.OUT)
GPIO.setup(comp,GPIO.IN)

try:
    while(1):
        for value in range(256):
            
            signal = num2dac(value)
            voltage = value* 3.3 / 256
            comparatorV = GPIO.input(comp)
            time.sleep(0.01)
            if comparatorV == 0:
                print("ADC value={:^3}->{}, input viltage = {:.2f}".format(value,signal,voltage))
                break
finally:
    GPIO.output(dac,clean)
    GPIO.cleanup()
