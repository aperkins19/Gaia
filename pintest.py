import RPi.GPIO as GPIO
import time

# Set the GPIO mode
GPIO.setmode(GPIO.BCM)

# Set up the GPIO pin for output
pin_to_test = 5  # Change to 3 for GPIO 3 test
GPIO.setup(pin_to_test, GPIO.OUT)

# Blink the LED
try:
    while True:
        print("High")
        GPIO.output(pin_to_test, GPIO.HIGH)  # LED on
        time.sleep(1)
        print("Low")
        GPIO.output(pin_to_test, GPIO.LOW)   # LED off
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()  # Clean up GPIO on CTRL+C exit