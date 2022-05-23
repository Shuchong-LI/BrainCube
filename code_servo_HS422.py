import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
servoPin = 11

GPIO.setup(servoPin,GPIO.OUT)
pwm = GPIO.PWM(servoPin,50)
pwm.start(7)

position = 100
for i in range(0,20):
    #position = input("position: degree from 0 to 180 ")
    DC = 1./18.*(position) + 2
    pwm.ChangeDutyCycle(DC)
pwm.stop()
GPIO.cleanup()