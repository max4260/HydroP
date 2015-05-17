import webiopi
from webiopi import deviceInstance
import sqlite3
import sys
import time

GPIO = webiopi.GPIO
tempSensor = deviceInstance("tmp")
interval = int(sys.argv[1])
SCRIPT_PATH = "/home/pi/HydroP/python/"

dbconn = sqlite3.connect(SCRIPT_PATH + "hydro.db")
dbconn.row_factory = sqlite3.Row
dbcursor = dbconn.cursor()

while (1 == 1):

	temp = tmp.getFahrenheit()
	rightNah = time.gmtime()
	c.execute("INSERT INTO temperatures('device', 'timestamp', 'temperature') VALUES (?, ?, ?);", ("TEMP1", rightNah, temp))
	dbconn.commit()
	webiopi.sleep(interval)