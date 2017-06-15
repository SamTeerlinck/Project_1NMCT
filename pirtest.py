import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(36, GPIO.IN)         #Read output from PIR motion sensor
for x in range(1, 27):
	GPIO.setup(x, GPIO.OUT)         #Touchscreen output pin
while True:
	i=GPIO.input(36)
	if i==0:	   #When output from motion sensor is LOW
		print "No intruders",i
		for x in range(1, 27):
			GPIO.output(x, 1)  #Turn OFF Screen
	elif i==1:               #When output from motion sensor is HIGH
		print "Intruder detected",i
		for x in range(1, 27):
				GPIO.output(x, 0)  #Turn ON Screen