import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
servoPin = 11

GPIO.setup(servoPin,GPIO.OUT)
pwm = GPIO.PWM(servoPin,50)
pwm.start(20)
time.sleep(2)

duty = 2

# 0 degree duty = 2 and 180 degree duty =12
pwm.ChangeDutyCycle(2)

temp = input("choose the temprature[0-250]:")
position = float(temp)*180/250
duty += position/18 

pwm.ChangeDutyCycle(duty)
time.sleep(3)

pwm.stop()
GPIO.cleanup()