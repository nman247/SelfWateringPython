##Coding Borrowed From FreeNove
##Requirements ADCDevice, ADC.py, 5VRelay, WaterPump, BatteryExternalSource, SoilMoistureSensor
##SDA1-SDA(ADC), 3V-VCC(ADC) Best To Do 3V on (+ and Blue)One Side and 5V on Other(Red), SCL1-SCL(ADC),
#GND-GND(ADC), A0(VDC) - AOUT(SoilMoistureSensor)
##5V - VCC(Relay), GND-GND(Relay), GPIO20-IN(Relay)
##COMMON(Relay) - BatterySource(Positive(Red)), NO(Relay)-Positive(WaterPump),
#GND - WaterPumpGND(Negative(Black)) 
import time
from ADCDevice import *
from waterpump import *
##Code used from Freenove
adc = ADCDevice() # Define an ADCDevice class object

def setup():
    global adc
    if(adc.detectI2C(0x48)): # Detect the pcf8591.
        adc = PCF8591()
    elif(adc.detectI2C(0x4b)): # Detect the ads7830
        adc = ADS7830()
    else:
        print("No correct I2C address found, \n"
        "Please use command 'i2cdetect -y 1' to check the I2C address! \n"
        "Program Exit. \n");
        exit(-1)
##Loop use to detect Voltage from Soil Moisture Meter and turn on WaterPump at a specific level        
def loop():
    value = adc.analogRead(0)
    print ('ADC Value : ', value)
    while value >= 80: ##MAKE 80 THE LEVEL
        print ('ADC Value : ', value)
        WaterPump.WaterOn()
        value = adc.analogRead(0)    # read the ADC value of channel 0
    WaterPump.WaterOff()
    WaterPump.WaterCleanUp()
    


    
if __name__ == '__main__':   # Program entrance
    print ('Program is starting ... ')
    setup()
    ##Sets a CurrentTime
    currentTime = int(time.localtime().tm_hour)
    keyinput = "null"; 
    print("Current Time is: "+str(currentTime))
    ##Creates a Endless Loop
    while(keyinput == "null"):
        ##Sets two times a day for the soil sensor to be used(it is suggested to not used Moisture Sensor continuously)
        if(currentTime == 12 or currentTime == 24):
            ##Tells Current Time at Beginning of Loop
            print("Current Time is: "+str(currentTime))
            ##Activate the Physical Loop of Project
            loop()
        ##Sets a time to ask the user if they want to continue the program
        ##Best to set at time User is present
        elif(currentTime == 13):
            print("A Full Day has Passed!")
            newkeyInput=input("Press Enter to End the Program (Put in a Input if you want to Continue the Program): ")
            ##Ends the loop
            if(newkeyInput == ""):
                break
            else:
                ###Waits a Hour before CurrentTime is checked again
                time.sleep(3600)
                currentTime = int(time.localtime().tm_hour)
                #Continues the Loop
                continue  
        currentTime = int(time.localtime().tm_hour)
         
    print("Program Ended!")
    
    
 