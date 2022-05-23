import time
import RPi.GPIO as GPIO
import grovepi
import os

servoPinTemp = 11
servoPinTimer = 13
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
    value = grovepi.analogRead(grove_force)
    #print("weight:" + str(value))
    time.sleep(0.2)
    return value
        
def servo():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(servoPinTemp,GPIO.OUT)
    GPIO.setup(servoPinTimer,GPIO.OUT)
    pwm1 = GPIO.PWM(servoPinTemp,50)
    pwm2 = GPIO.PWM(servoPinTimer,50)
    pwm1.start(20)
    pwm2.start(20)
    time.sleep(2)   
    duty1 = 2
    duty2 = 2
# 0 degree duty = 2 and 180 degree duty =12
    pwm1.ChangeDutyCycle(2)
    pwm2.ChangeDutyCycle(2)

    temp = input("choose the temprature[0-250]:")
    position1 = float(temp)*180/250
    duty1 += position1/18
    
    timer = input("choose the time[0-9]:")
    position2 = float(timer)*180/9
    duty2 += position1/18 

    pwm1.ChangeDutyCycle(duty1)
    time.sleep(1)
    pwm2.ChangeDutyCycle(duty2)
    time.sleep(1)

    pwm1.stop()
    pwm2.stop()
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
    servo()
    while(1):
        try:
            print("----------------------")
            w = poid()           
            print("weight:" + str(w))
            #d = telemetre()
            #print('Distance:',d,'cm')
            DHT()
            
        except IOError:
            print("error")