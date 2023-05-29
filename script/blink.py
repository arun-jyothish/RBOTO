import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep # Import the sleep function from the time module

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use Broadcom pin numbering
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)
servo_pin = 23
while True: # Run forever
    GPIO.output(servo_pin, GPIO.HIGH) # Turn on
    sleep(1) # Sleep for 1 second
    GPIO.output(servo_pin, GPIO.LOW) # Turn off
    sleep(1) # Sleep for 1 second
