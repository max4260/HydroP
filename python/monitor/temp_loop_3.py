import webiopi
from webiopi import deviceInstance
import sqlite3
import sys
import time

GPIO = webiopi.GPIO
tempSensor = deviceInstance("tmp")
SCRIPT_PATH = "/home/pi/HydroP/python/"

dbconn = sqlite3.connect(SCRIPT_PATH + "hydro.db")
dbconn.row_factory = sqlite3.Row
dbcursor = dbconn.cursor()

dbcursor.execute("SELECT status, interval FROM devices WHERE name = 'TEMP3' VALUES (?, ?);", (status, interval))


while (status == 1):

	temp = tempSensor.getFahrenheit()
	rightNah = time.gmtime()
	dbcursor.execute("INSERT INTO temperatures('device', 'timestamp', 'temperature') VALUES (?, ?, ?);", ("TEMP3", rightNah, temp))
	dbconn.commit()
	webiopi.sleep(interval)