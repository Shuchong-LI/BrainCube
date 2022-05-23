import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
servoPin = 12

GPIO.setup(servoPin,GPIO.OUT)
pwm = GPIO.PWM(servoPin,50)
pwm.start(20)
time.sleep(2)

duty = 2

# 0 degree duty = 2 and 180 degree duty =12
pwm.ChangeDutyCycle(2)

temp = input("choose the time[0-9]:")
position = float(temp)*180/9
duty += position/18 

pwm.ChangeDutyCycle(duty)
time.sleep(3)

pwm.stop()
GPIO.cleanup()