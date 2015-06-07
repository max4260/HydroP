HydroP
=========
*https://github.com/max4260/HydroP*

## Description:
This is a Raspberry Pi hydroponics controller.

## Version History
* _v0.02.00_ - **2015-06-07**:
	
	>Updated UI to BootStrap.
	>>Dashboard - Added;
	>>Charts - Added;
	>>Setting - Added; layout has mostly been completed
	
* _v0.01.01_ - **2015-05-17**:
	
	>Added framework for controlling external hardware.
	>Added SQLite framework.

* _v0.00.01_ - **2015-04-17**:
	
	>First commit.
	


## TODO List:
1. Update UI:
	
	>i. 'Dashboard' - layout needs work.
	
	>ii. 'Graphs' - layout needs lots of work.
	
	>iii. 'Settings' - layout is mostly complete.
	
	>>a. Add connected & GPIO pin selector for every input

2. Update Functionality
	
	>i. 'Dashboard' - Functionality is not ready to start.
	
	>ii. 'Graphs' - Functionality is not ready to start.
	
	>iii. 'Settings' - Functionality is ready to start.
	
	>>a. 'Temperature' - DS18b20
	
	>>>A. Read up to (4) sensors on interval
	
	>>>B. Update current VALUE to screen
	
	>>>C. Save LOW/HIGH warning values from user to DB
	
	>>>D. Monitor current VALUE vs user selected range
	
	>>b. 'Humidity' 
	
	>>>A. Buy sensor
	
	>>>B. Read up to (4) sensors on interval
	
	>>>C. Update current VALUE to screen
	
	>>>D. Save LOW/HIGH warning values from user to DB
	
	>>>E. Monitor current VALUE vs user selected range
	
	>>c. 'TDS' - Not ready for development.
	
	>>d. 'CO2' - Not ready for development.
	
	>>e. 'Light' - Not ready for development.
	
	
	
## Future List:
Graph all data

email support

LCD touch screen

Input control for: Temp(4), Light(2), Humidity(2), TDS(2), CO2(2)

Advanced input control for: water level(2), PH(2)

Output control for: light(1), water pump(1)

Advanced output control for: nutrient mixing(1), heater(1), AC(1), Humidifier(1), Dehumidifier(1), CO2(1)