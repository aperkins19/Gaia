import RPi.GPIO as GPIO  # interact with Pis pins
import time

# setup pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

# run
GPIO.output(18, GPIO.LOW)

for i in range(0, 100, 1):

    GPIO.output(18, GPIO.HIGH)

    time.sleep(2)

    GPIO.output(18, GPIO.LOW)

    time.sleep(2)

GPIO.cleanup()