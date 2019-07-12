from gpiozero import LED
from time import sleep

led = LED(17)

while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)

from subprocess import call

def print_thing():
    print ("button pressed")

button.when_pressed = print_thing
