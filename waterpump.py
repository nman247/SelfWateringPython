##Created by Nasir Martin
import RPi.GPIO as GPIO
import time
class WaterPump:
    
    def WaterOn():
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        print("Water Pump On")
        GPIO.setup(20,GPIO.OUT)
        GPIO.setup(20,GPIO.LOW)
    
    def WaterOff():
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        print("Water Pump Off")
        GPIO.setup(20,GPIO.HIGH)
    def WaterCleanUp():
        GPIO.cleanup()



        



        



    


