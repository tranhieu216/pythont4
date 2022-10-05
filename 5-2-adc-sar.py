import RPi.GPIO as GPIO
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]
leds = [21, 20, 16, 12, 7, 8, 25, 24]
bits = len(dac)
levels = 2**bits
maxVoltage = 3.3
troykaModule = 17
comparator = 4


GPIO.setmode(GPIO.BCM)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(dac, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(troykaModule, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comparator, GPIO.IN)

def d2b(decimal):
    return [int(bit) for bit in bin(decimal)[2:].zfill(bits)]

def num2dac(value):
    signal = d2b(value)
    GPIO.output(dac, signal)
    return signal

def adc(comparator, dac):
    value = 0
    v1 = 0
    for i in range(8):
        v1 = value + 2 ** (7 - i)
        if v1 < 256:
            signal = d2b(v1)
            GPIO.output(dac, signal)
            time.sleep(0.05)
            comparatorvalue = GPIO.input(comparator)
            if comparatorvalue == 1:
                value = v1
    return value

try:
    while True:
        a = (adc(comparator, dac))
        a1 = a
        k = 250 / 8
        for t in leds:
            if a1 > k:
                GPIO.output(t, 1)
                a1 -= k
            else:
                GPIO.output(t, 0)
        print("digital-", a, "voltage", end = " ")
        print("{:.3f}".format(a * 3.3 / 2 ** 8))
        
finally:
    GPIO.output(dac, 0)
    GPIO.output(troykaModule, 0)
    GPIO.output(leds, 0)
    GPIO.cleanup()
