import time
import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADS1015 ADC instance
ads = ADS.ADS1015(i2c)

# Create an analog input channel on the ADS1015
chan = AnalogIn(ads, ADS.P0) # Assuming you're using channel 0

while True:
    print("Moisture Level:", chan.value, "Raw ADC Value:", chan.voltage)
    time.sleep(1)