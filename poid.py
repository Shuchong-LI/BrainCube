import time
import RPi.GPIO as GPIO
import grovepi


grove_force = 0


grovepi.pinMode(grove_force,"INPUT")

if __name__ == "__main__":
	#print("hello")
    while(1):
        try:
            value = grovepi.analogRead(grove_force)
            time.sleep(0.1)
        except IOError:
            print("error")