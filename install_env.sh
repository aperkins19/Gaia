#! /bin/bash

apt -y update
apt install -y python3-smbus i2c-tools

# python packages

# ADS analog to digital driver
pip3 install adafruit-circuitpython-ads1x15

