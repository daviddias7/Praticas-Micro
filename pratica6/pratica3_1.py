from gpiozero import PWMLED
from time import sleep

pin = 18
led = PWMLED(pin)

while True:
    sleep(0.005)
    for b in range (101):
        led.value = b / 100.0
        sleep(0.005)
