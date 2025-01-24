#!/usr/bin/env python
#
'''
Simple program to extract Midnite Classic solar charge controller using classic_modbusdecoder.py module.

Based on the following Github repository:

https://github.com/ClassicDIY/ClassicMQTT/blob/master/code/Python/support/classic_modbusdecoder.py

'''

from classic_modbusdecoder import getModbusData
import pprint  
import logging


'''logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)-5s %(module)s:%(lineno)s %(message)s",
)'''


data = {}
data1 = {}
# Need to supply IP address and port number. In this example, there are two Midnite Classic 150
# solar charge controllers.
data = getModbusData(False, "192.168.20.10", 502)
print("\nClassic1: ", data)
pprint.pp(data)
print(
    "\n\n=================================================================================\n\n"
)

data1 = getModbusData(False, "192.168.20.12", 502)
print("\nClassic2: ", data1)
pprint.pp(data1)
print("Done...")
