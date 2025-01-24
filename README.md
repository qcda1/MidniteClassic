# MidniteClassic
## Simple module to extract Midnite Classic set of registers for monitoring using Modbus over Ethernet.

It is based on https://github.com/ClassicDIY/ClassicMQTT with a few enhancements such as:
- expanded decoded text
- fixed AUX1 and AUX2 states
- Added log statement to help in debugging
- Extracted Payload.py from pymodbus where it is being deprecated
- Kept it simple as a tool to easily get Midnite Classic solar charge controller's data
