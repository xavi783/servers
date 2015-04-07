import RPi.GPIO as GPIO
import time

GPIO.setup(3, GPIO.OUT)

while i < 10:
	GPIO.output(3, True)
	time.sleep(1000)
	GPIO.output(3, False)