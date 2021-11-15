##Created by Nasir Martin
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
class WaterPump:
    def WaterOn():
        print("Water Pump On")
        GPIO.setup(20,GPIO.OUT)
        GPIO.setup(20,GPIO.LOW)
    
    def WaterOff():
        print("Water Pump Off")
        GPIO.setup(20,GPIO.HIGH)
    def WaterCleanUp():
        GPIO.cleanup()

WaterPump.WaterOff()

        



    


