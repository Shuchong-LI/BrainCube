import time
import RPi.GPIO as GPIO
import grovepi


grove_force = 14


grovepi.pinMode(grove_force,"INPUT")
time.sleep(2)
if __name__ == "__main__":
    print("hello")
    while(1):
        try:
            value = grovepi.analogRead(grove_force)
            print("weight:" + str(value))
            time.sleep(0.2)
        except IOError:
            print("error")