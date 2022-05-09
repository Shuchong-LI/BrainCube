import time
import RPi.GPIO as GPIO
import grovepi

servoPin = 11
grove_force = 17
TRIG = 23
ECHO = 24


def poid():
    grovepi.pinMode(grove_force,"INPUT")
    value = grovepi.analogRead(grove_force)
    #print("weight:" + str(value))
    time.sleep(0.2)
    return value
        
def servo():
    GPIO.setmode(GPIO.BOARD)
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
        #GPIO.cleanup()
    
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
    #servo()
    while(1):
        try:
            print("----------------------")
            w = poid()           
            print("weight:" + str(w))
            d = telemetre()
            print('Distance:',d,'cm')
            
            
        except IOError:
            print("error")