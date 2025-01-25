#!/usr/bin/env python
#
'''
Simple program to extract Midnite Classic solar charge controller data using classic_modbusdecoder.py module.

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
for IP in ('192.168.20.10', '192.168.20.12'):
    print("\n\n=================================================================================")
    data = getModbusData(False, IP, 502)
    print(f"{data['Name']}:")
    pprint.pp(data)

print("Done...")
