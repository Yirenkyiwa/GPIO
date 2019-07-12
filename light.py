from gpiozero import LED
from gpiozero import LED, Button
from time import sleep
from subprocess import call
button = Button(2)
led = LED(17)
led1 = LED1(30)
led2 = LED2(9)

def print_thing():
    print ("button pressed")

button.when_pressed = print_thing

while True:
    led.on()
    sleep(1)
    led1.on()
    sleep(1)
    led2.on()
    sleep(1)
    led.off()
    sleep(1)
    led1.off()
    sleep(1)
    led2.off()
    sleep(1)
