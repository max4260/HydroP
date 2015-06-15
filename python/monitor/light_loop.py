import webiopi
import sys

GPIO = webiopi.GPIO
LIGHT = 17
interval = int(sys.argv[1])

while (1 == 1):
	opposite = GPIO.digitalRead(LIGHT)

	if (opposite == GPIO.HIGH):
		opposite = GPIO.LOW
	else:
		opposite = GPIO.HIGH
		
	GPIO.digitalWrite(LIGHT, opposite)
	webiopi.sleep(interval)