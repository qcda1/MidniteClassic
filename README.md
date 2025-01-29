# MidniteClassic
## Simple module to extract Midnite Classic set of registers for monitoring using Modbus over Ethernet.

It is based on https://github.com/ClassicDIY/ClassicMQTT with a few enhancements such as:
- expanded decoded text
- fixed AUX1 and AUX2 states
- Added log statement to help in debugging
- Extracted Payload.py from pymodbus where it is being deprecated
- Kept it simple as a tool to easily get Midnite Classic solar charge controller's data

The output of the function is a dictionary with value names as keys and decoded values as values for example:
{'PCB': 4, 'Type': 150, 'Year': 2018, 'Month': 2, 'Day': 6, 'InfoFlagBits3': 15, 'ignore': None, 'mac_1': 46, 'mac_0': 230, 'mac_3': 15, 'mac_2': 0, 'mac_5': 96, 'mac_4': 29, 'ignore2': None, 'unitID': 3957535947, 'StatusRoll': 20494, 'RsetTmms': 1, 'BatVoltage': 55.1, 'PVVoltage': 90.3, 'BatCurrent': 2.1, 'EnergyToday': 2.2, 'Power': 116.0, 'ChargeStage': 5, 'State': 4, 'PVCurrent': 1.4, 'lastVOC': 91.2, 'HighestVinputLog': 1465, 'MatchPointShadow': 0, 'AmpHours': 41, 'TotalEnergy': 7770.6, 'LifetimeAmpHours': 149500, 'InfoFlagsBits': 2986348548, 'BatTemperature': 10.0, 'FETTemperature': 39.8, 'PCBTemperature': 43.4, 'NiteMinutesNoPwr': 0, 'MinuteLogIntervalSec': 300, 'modbus_port_register': 502, 'FloatTimeTodaySeconds': 12002, 'AbsorbTime': 3600, 'reserved1': 21, 'PWM_ReadOnly': 859, 'Reason_For_Reset': 4, 'EqualizeTime': 5400, 'WbangJrCmdS': 53, 'WizBangJrRawCurrent': -1, 'skip': None, 'WbJrAmpHourPOSitive': 30273, 'WbJrAmpHourNEGative': -27048, 'WbJrAmpHourNET': 3225, 'WhizbangBatCurrent': 0.0, 'WizBangCRC': -90, 'ShuntTemperature': 13.0, 'SOC': 100, 'skip2': None, 'RemainingAmpHours': 400, 'skip3': None, 'TotalAmpHours': 400, 'MPPTMode': 11, 'Aux12Function': 4625, 'Name0': 76, 'Name1': 67, 'Name2': 83, 'Name3': 65, 'Name4': 73, 'Name5': 83, 'Name6': 49, 'Name7': 67, 'CTIME0': 51251732, 'CTIME1': 132710680, 'CTIME2': 4293394733, 'VbattRegSetPTmpComp': 55.2, 'nominalBatteryVoltage': 48, 'endingAmps': 4.0, 'ReasonForResting': 38, 'app_rev': 2193, 'net_rev': 2122, 'IP': '192.168.20.10', 'MAC': '60:1D:0F:00:2E:E6', 'Name': 'CLASSIC1', 'ChargeStateIcon': 'mdi:format-float-center', 'ChargeStateText': 'Float', 'Aux1OffAutoOn': 0, 'Aux1Function': 17, 'Aux1FunctionText': 'FLOAT HIGH', 'Aux1OffAutoOnText': 'AUX Off', 'Aux2OffAutoOn': 0, 'Aux2Function': 18, 'Aux2FunctionText': 'Whizbang Junior (WB Jr.)', 'Aux2OffAutoOnText': 'AUX Off', 'MPPTModeText': 'SOLAR', 'SOCicon': 'mdi:battery', 'ReasonForRestingText': 'Unknown code: 38'}

Program classic.py is an example of data extraction on a two solar charge controller set up.

Notes:
- The module only support Ethernet attached solar charge controllers
- It does not support writing to registers for now.
