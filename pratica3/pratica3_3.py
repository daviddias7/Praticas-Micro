import Adafruit_DHT
import RPi.GPIO as GPIO
import time

sensor = Adafruit_DHT.DHT11

pino_GPIO = 20

try:
	while True:
		humidity, temperature = Adafruit_DHT.read_retry(sensor, pino_GPIO)
		print('Temperatura: ' + str(temperature) + '°C')
		print('Humidade: ' + str(humidity) + '%')
		time.sleep(0.1)
except keyboardInterrupt:
	GPIO.cleanup()
	exit()
