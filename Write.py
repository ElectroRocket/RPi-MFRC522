# Write your code here :-)
import RPi.GPIO as GPIO
import SimpleMFRC522

reader = SimpleMFRC522.SimpleMFRC522()

try:
        text = raw_input('Enter New Data to write to card: ')
        print("Now place your tag to write...")
        reader.write(text)
        print("Data written successfully")
finally:
        GPIO.cleanup()
