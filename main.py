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
        
def loop():
    value = adc.analogRead(0)
    print ('ADC Value : ', value)
    while value >= 80: ##MAKE 80 THE LEVEL
        value = adc.analogRead(0)    # read the ADC value of channel 0
        print ('ADC Value : ', value)
        WaterPump.WaterOn()
    WaterPump.WaterOff()
    WaterPump.WaterCleanUp()
    adc.close()


    
if __name__ == '__main__':   # Program entrance
    print ('Program is starting ... ')
    setup()
    loop()
    
 
