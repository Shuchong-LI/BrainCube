import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
servoPin = 11

GPIO.setup(servoPin,GPIO.OUT)
pwm = GPIO.PWM(servoPin,50)
pwm.start(0)
time.sleep(2)

duty = 2
#from 0 degree to 180 degree
while duty <= 12:
    pwm.ChangeDutyCycle(duty)
    time.sleep(1)
    duty = duty + 1
    
time.sleep(2)

#back to 0 degree
pwm.ChangeDutyCycle(2)

time.sleep(1)
pwm.ChangeDutyCycle(0)

pwm.stop()
GPIO.cleanup()