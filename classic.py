#!/usr/bin/env python
#
'''
Simple program to extract Midnite Classic solar charge controller data
using classic_modbusdecoder.py module.

Based on the following Github repository:

https://github.com/ClassicDIY/ClassicMQTT

'''

from classic_modbusdecoder import getModbusData
import pprint  
import logging

# Uncomment the following to see debug data as the program runs
'''logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)-5s %(module)s:%(lineno)s %(message)s",
)'''

# The function only need the IP address of the solar charge controller and
# return a dict will all decoded register values and their name as keyes.
data = {}
for IP in ('192.168.20.10', '192.168.20.12'):
    print("\n\n=================================================================================")
    data = getModbusData(False, IP, 502)
    print(f"{data['Name']}:")
    pprint.pp(data)

print("Done...")
