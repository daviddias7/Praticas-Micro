from gpiozero import PWMLED
from time import sleep

pin = 21
led = PWMLED(pin)

for b in range (101):
    led.value = b / 100.0
    sleep(0.1)
