import time
import Adafruit_ADS1x15

# Create the I2C bus
adc = Adafruit_ADS1x15.ADS1115()
GAIN=1
value = adc.read_adc(0, gain=GAIN)