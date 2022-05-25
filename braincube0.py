import time
import RPi.GPIO as GPIO
import grovepi
import os

servoPinTemp = 13
servoPinTimer = 11
servoPinTour = 12
grove_force = 14
TRIG = 23
ECHO = 24

def DHT():
    ficher = os.popen("./test")
    res = ficher.read()
    print(res)
    ficher.close()
    
def poid():
    grovepi.pinMode(grove_force,"INPUT")
    value = float(grovepi.analogRead(grove_force))/325
    #print("weight:" + str(value))
    time.sleep(0.2)
    return value
        
def servoTemp(temp):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(servoPinTemp,GPIO.OUT)
    
    pwm1 = GPIO.PWM(servoPinTemp,50)

    pwm1.start(0)
    time.sleep(1)   
    duty1 = 2
# 0 degree duty = 2 and 180 degree duty =12
    pwm1.ChangeDutyCycle(2)

    #temp = input("choose the temprature[0-250]:")
    position1 = float(temp)*180/250
    duty1 += position1/18
    

    pwm1.ChangeDutyCycle(duty1)
    time.sleep(1)

    pwm1.stop()
   
    GPIO.cleanup()

def servoTimer(timer):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(servoPinTimer,GPIO.OUT)
    pwm2 = GPIO.PWM(servoPinTimer,50)

    pwm2.start(0)
    time.sleep(1)   
    duty2 = 2
# 0 degree duty = 2 and 180 degree duty =12
    pwm2.ChangeDutyCycle(2)

    #timer = input("choose the time[0-9]:")
    position2 = float(timer)*180/9
    duty2 += position2/18 

    pwm2.ChangeDutyCycle(duty2)
    time.sleep(1)

    pwm2.stop()
   
    GPIO.cleanup()

def servoTour(tour):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(servoPinTour,GPIO.OUT)
    
    pwm1 = GPIO.PWM(servoPinTour,50)

    pwm1.start(0)
    time.sleep(1)   
    duty1 = 2
# 0 degree duty = 2 and 180 degree duty =12
    pwm1.ChangeDutyCycle(2)

    position1 = float(tour)*90
    duty1 += position1/18
    

    pwm1.ChangeDutyCycle(duty1)
    time.sleep(1)

    pwm1.stop()
   
    GPIO.cleanup()
def telemetre():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.setup(ECHO,GPIO.IN)
    GPIO.output(TRIG, False)
    
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    while GPIO.input(ECHO)==0:
        pulse_start = time.time()
    while GPIO.input(ECHO)==1:
        pulse_end = time.time()
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17165
    distance = round(distance, 1)
    #print ('Distance:',distance,'cm')
    #GPIO.cleanup()
    time.sleep(1)
    return distance


if __name__ == "__main__":
    servoTemp(0)
    servoTimer(0)
   # servoTour(0)
    while(1):
        try:
            print("-------------------")
            w = poid()
            w =round(w/3, 2)
            print("weight:" + str(w),"kg")
            d = telemetre()
            d = round(1 - 25.0/d,1)
            print('pate reste:',d,'%')
            DHT()
            
        except IOError:
            print("error")