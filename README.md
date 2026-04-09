# MidniteClassic

## Simple module to extract Midnite Classic set of registers for monitoring using Modbus over Ethernet.

It is based on [ClassicMQTT](https://github.com/ClassicDIY/ClassicMQTT) with a few enhancements such as:

- expanded decoded text
- fixed AUX1 and AUX2 states
- Added log statement to help in debugging
- Extracted Payload.py from pymodbus where it is being deprecated
- Kept it simple as a tool to easily get Midnite Classic solar charge controller's data in a Python program

The output of the function is a dictionary with value names as keys and decoded values as values for example:
{'PCB': 4, 'Type': 150, 'Year': 2018, 'Month': 2, 'Day': 6, 'InfoFlagBits3': 15, 'ignore': None, 'mac_1': 46, 'mac_0': 230, 'mac_3': 15, 'mac_2': 0, 'mac_5': 96, 'mac_4': 29, 'ignore2': None, 'unitID': 3957535947, 'StatusRoll': 12288, 'RsetTmms': 1, 'BatVoltage': 53.3, 'PVVoltage': 74.1, 'BatCurrent': 5.8, 'EnergyToday': 0.3, 'Power': 310.0, 'ChargeStage': 4, 'State': 3, 'PVCurrent': 4.3, 'lastVOC': 86.6, 'HighestVinputLog': 1465, 'MatchPointShadow': 0, 'AmpHours': 6, 'TotalEnergy': 8493.9, 'LifetimeAmpHours': 163127, 'InfoFlagsBits': 2986348548, 'BatTemperature': 16.2, 'FETTemperature': 42.2, 'PCBTemperature': 47.0, 'NiteMinutesNoPwr': 0, 'MinuteLogIntervalSec': 300, 'modbus_port_register': 502, 'FloatTimeTodaySeconds': 0, 'AbsorbTime': 3593, 'reserved1': 58, 'PWM_ReadOnly': 1043, 'Reason_For_Reset': 4, 'EqualizeTime': 5400, 'WbangJrCmdS': 53, 'WizBangJrRawCurrent': -91, 'skip': None, 'WbJrAmpHourPOSitive': 52236, 'WbJrAmpHourNEGative': -48498, 'WbJrAmpHourNET': 3737, 'WhizbangBatCurrent': 7.6, 'WizBangCRC': 109, 'ShuntTemperature': 23.0, 'SOC': 89, 'skip2': None, 'RemainingAmpHours': 448, 'skip3': None, 'TotalAmpHours': 500, 'AbsorbVoltageSetPoint': 56.0, 'FloatVoltageSetPoint': 55.2, 'EqualizeVoltageSetPoint': 56.1, 'EualizeTime': 5400, 'EqualiseIntervalDay': 0, 'MPPTMode': 11, 'Aux12Function': 4625, 'Name0': 76, 'Name1': 67, 'Name2': 83, 'Name3': 65, 'Name4': 73, 'Name5': 83, 'Name6': 49, 'Name7': 67, 'CTIME0': 34093088, 'CTIME1': 132776969, 'CTIME2': 4292411403, 'VbattRegSetPTmpComp': 56.0, 'nominalBatteryVoltage': 48, 'endingAmps': 2.0, 'ReasonForResting': 5, 'DaysBetweenBulkAbsorb': 0, 'app_rev': 2193, 'net_rev': 2122, 'IP': '192.168.20.10', 'MAC': '60:1D:0F:00:2E:E6', 'Name': 'CLASSIC1', 'ChargeStateIcon': 'mdi:battery-charging', 'ChargeStateText': 'Bulk MPPT', 'Aux1OffAutoOn': 0, 'Aux1Function': 17, 'Aux1FunctionText': 'FLOAT HIGH', 'Aux1OffAutoOnText': 'AUX Off', 'Aux2OffAutoOn': 0, 'Aux2Function': 18, 'Aux2FunctionText': 'Whizbang Junior (WB Jr.)', 'Aux2OffAutoOnText': 'AUX Off', 'MPPTModeText': 'SOLAR', 'SOCicon': 'mdi:battery-charging-80', 'ReasonForRestingText': ' Too low of power out and Vbatt below set point for > 90 seconds'}


Program classic.py is an example of data extraction on a two solar charge controller set up. Edit the code with your Classic's IP address

Notes:

- The module only support Ethernet attached solar charge controllers
- It does not support writing to registers for now.

## Installation

Two KISS approaches.

1- CLone the repo
You can clone this repo on your system. It will copy all the content.
You will need pymodbus module as well: pip install pymodbus

2- Download just the necessary files
You will need pymodbus module:
pip install pymodbus

In the repo, you will find a bash script that will download the necessary modules to get things underway. the bash script "dload.sh" can be downloaded with the following command from your computer:

    curl -O "https://raw.githubusercontent.com/qcda1/MidniteClassic/main/dload.sh"

Make sure the bash script is executable: chmod +x dload.sh

Run the script from your working directory: ./dload.sh

This will download classic_modbusdecoder.py and Payload.py


Once you have the repo or just the necessary files in your system, you can take a copy of the classic.py program and modify it for your environment (IP address of the Classic). This simple program will quickly confirm if everything is working.


