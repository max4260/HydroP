import webiopi
import datetime
import sqlite3
import subprocess
import sys

GPIO = webiopi.GPIO
AUTO = 1
SCRIPT_PATH = "/home/pi/HydroP/python/"

LIGHT1 = 17 # GPIO pin using BCM numbering

dbconn = sqlite3.connect(SCRIPT_PATH + "hydro.db")
dbconn.row_factory = sqlite3.Row
dbcursor = dbconn.cursor()

# setup function is automatically called at WebIOPi startup
def setup():
    # set the GPIO used by the light to output
    GPIO.setFunction(LIGHT1, GPIO.OUT)

    # retrieve current datetime
    now = datetime.datetime.now()
	
    dbcursor.execute("SELECT status, interval FROM devices WHERE name = \"LIGHT1\"")
    lightDevice = dbcursor.fetchone()
    
    if (lightDevice != None) and (lightDevice["status"] == AUTO):
        setLightInterval(lightDevice['interval'])

# loop function is repeatedly called by WebIOPi 
def loop():
    # retrieve current datetime
    now = datetime.datetime.now()

    # gives CPU some time before looping again
    webiopi.sleep(1)

# destroy function is called at WebIOPi shutdown
def destroy():
    GPIO.digitalWrite(LIGHT1, GPIO.LOW)

@webiopi.macro
def setLightInterval(interval):
	subprocess.Popen(["python",SCRIPT_PATH + "light_loop.py",str(interval)])