import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
servoPin = 11

GPIO.setup(servoPin,GPIO.OUT)
pwm = GPIO.PWM(servoPin,50)
pwm.start(6)
time.sleep(2)


pwm.stop()
GPIO.cleanup()