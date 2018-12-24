import RPi.GPIO as GPIO 
import SimpleMFRC522

reader = SimpleMFRC522.SimpleMFRC522()

#Welcome message
print("Looking for cards")
print("press ctrl+c to stop")

try:
            id, text = reader.read()
            print(id)
            print(text)
finally:
        GPIO.cleanup()