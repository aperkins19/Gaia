import time
import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADS1015 ADC instance
ads = ADS.ADS1015(i2c)

# Create an analog input
If the component you are using is an ADS1015 instead of an ADS1115, there are some differences you need to account for in your setup and code. Both are analog-to-digital converters from the same family but have different resolutions: the ADS1015 is a 12-bit ADC, while the ADS1115 is a 16-bit ADC.

Here are the steps to adjust your setup for an ADS1015:

### 1. **Update Your Python Script**
Since the ADS1015 has a different resolution, you should ensure that your Python script accounts for this. The good news is that the Adafruit CircuitPython library for the ADS1x15 series supports both the ADS1015 and ADS1115, but you may need to adjust the code slightly.

For an ADS1015, your script might look like this:

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