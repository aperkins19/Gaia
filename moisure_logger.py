import RPi.GPIO as GPIO  # interact with Pis pins
import time

# setup pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

#motor sig
GPIO.setup(23, GPIO.OUT)

# run
GPIO.output(18, GPIO.LOW)
GPIO.output(23, GPIO.LOW)


time.sleep(5)
GPIO.output(23, GPIO.HIGH)
time.sleep(5)
GPIO.output(23, GPIO.LOW)



for i in range(0, 3, 1):

    GPIO.output(18, GPIO.HIGH)

    time.sleep(2)

    GPIO.output(18, GPIO.LOW)

    time.sleep(2)

GPIO.cleanup()